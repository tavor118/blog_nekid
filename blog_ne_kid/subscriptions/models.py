"""Models for subscription application."""

from django.db import models
from django.conf import settings

from blogs.models import Post, Blog


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
