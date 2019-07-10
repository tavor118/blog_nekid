"""Models for subscription application."""

from django.db import models
from django.conf import settings

from blogs.models import Post, Blog
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Subscription(models.Model):
    """
    Model for implementation subscription functionality.
    Bind blog and user, who follow given blog.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='subscriptions',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='subscriptions',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} follows {self.blog}."


class IsReadPost(models.Model):
    """
    Model for implementation reading post functionality.
    """
    subscription = models.ForeignKey(
        Subscription,
        related_name='read_posts',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='read_posts',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.post} is read by {self.subscription.user}"


@receiver(post_save, sender=Post)
def send_message_to_followers(sender, instance, created, **kwargs):
    """Send notification to followers after post creating."""
    if created:
        users = User.objects.filter(subscriptions__blog=instance.blog)
        for user in users:
            user.profile.send_notification_about_new_post()
