"""Models for users application."""

from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.services import send_notification_email


class UserManager(BaseUserManager):
    """Define a model manager for User model."""

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """Create and save a User with the given username, email and password."""
        if not username:
            raise ValueError('The given username must be set')

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """Create and save a regular User with the given username, email and password."""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """Create and save a SuperUser with the given username, email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    Extending the base class that Django has for User models.
    Required fields: 'username', 'email' , 'password'.
    """
    email = models.EmailField(
        _('Email address'), max_length=50, unique=True,
    )

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """Model for additional information about user."""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    )
    title = models.CharField(max_length=50, blank=True, default="")
    about = models.TextField(blank=True, default="")

    def send_notification_about_new_post(self):
        """
        Get notification about new post.
        """
        return send_notification_email(self.user)

    @property
    def get_followers(self):
        """
        Get list of followers.
        """
        return User.objects.filter(subscriptions__user=self.user)


# Define signals so our UserProfile model
# will be automatically created/updated
# when we create/update User instances.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create profile after user creating."""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save profile after user creating."""
    instance.profile.save()
