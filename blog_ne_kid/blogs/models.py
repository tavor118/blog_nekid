"""Models for blogs application."""

from django.conf import settings
from django.db import models

from django_extensions.db.models import TimeStampedModel


class Blog(TimeStampedModel, models.Model):
    """Model for blogs."""
    name = models.CharField(max_length=50, unique=True)
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='blogs',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created"]


class Post(TimeStampedModel, models.Model):
    """Model for posts."""

    title = models.CharField(max_length=50, unique=True)
    body = models.TextField(max_length=500)
    blog = models.ForeignKey(
        Blog, related_name='posts', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created"]
