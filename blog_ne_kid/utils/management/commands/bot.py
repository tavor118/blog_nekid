"""
Custom management command for creating users, blogs and subscriptions for them.
Run:
`python manage.py bot`
"""

import json
import os
import random
from django.core.management.base import BaseCommand

from seed import factories

from config.settings import BASE_DIR


def get_configuration():
    """
    Get configuration for bot from `bot_config.json` file.
    :return: Dictionary with configurations.
    """
    config_file = os.path.join(BASE_DIR, 'bot_config.json')
    with open(config_file) as config:
        return json.load(config)


def create_users(number_of_users):
    """
    Create given number of users.
    :param number_of_users:
    :return: Created users.
    """
    users = factories.UserFactory.create_batch(number_of_users)
    return users


def create_posts(max_posts_per_user, users):
    """
    Create posts.
    :param max_posts_per_user: Maximum posts per user.
    :param users: List of users.
    :return: Created posts.
    """
    all_posts = []
    for user in users:
        posts = factories.PostFactory.create_batch(
            random.randint(0, max_posts_per_user), blog=user.blogs
        )
        all_posts += posts
    return all_posts


def create_subscriptions(max_subscriptions_per_user, users):
    """
    Create likes.
    :param max_subscriptions_per_user: Maximum subscriptions per user.
    :param users: List of users.
    :return: Created subscriptions.
    """
    subscription_list = []
    for user in users:
        subscriptions_per_user = random.randint(0, max_subscriptions_per_user)
        blogs_drafts = [user.blogs for user in users]
        random.shuffle(blogs_drafts)
        for _ in range(subscriptions_per_user):
            subscription = factories.SubscriptionFactory(
                user=user, blog=blogs_drafts.pop()
            )
            subscription_list.append(subscription)
            if not blogs_drafts:
                break
    return subscription_list


class Command(BaseCommand):
    """
    Custom management command for creating users, posts and subscriptions for them.
    """

    help = 'Bot for creating users, posts and likes for them.'

    def handle(self, *args, **kwargs): #pylint: disable=unused-argument

        config = get_configuration()
        users = create_users(config['number_of_users'])
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created such users: {users}.'
        ))

        posts = create_posts(config['max_posts_per_user'], users)
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created such posts: {posts}.'
        ))

        subscription_list = create_subscriptions(config['max_posts_per_user'], users)
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created such subscriptions: {subscription_list}.'
        ))
