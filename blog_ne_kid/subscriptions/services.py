"""
Additional functions for working with "subscription" functionality.
"""

from .models import Subscription, IsReadPost


def subscribe(blog, user):
    """
    Subscribe on blog.
    """
    return Subscription.objects.get_or_create(
        blog=blog,
        user=user
    )


def unsubscribe(blog, user):
    """
    Remove a subscription.
    """
    Subscription.objects\
        .filter(blog=blog, user=user)\
        .delete()


def mark_as_read(post, subscription):
    """
    Mark post as read in news feed.
    """
    return IsReadPost.objects.get_or_create(
        post=post,
        subscription=subscription
    )
