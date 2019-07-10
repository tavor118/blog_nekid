"""Factories for creating fake data."""

import factory
from faker import Factory

from blogs.models import Blog, Post
from subscriptions.models import Subscription, IsReadPost
from users.models import User, UserProfile

faker = Factory.create()


class UserProfileFactory(factory.DjangoModelFactory):
    """Factory for user profile creating."""

    class Meta:
        model = UserProfile
        django_get_or_create = ('user',)

    title = factory.LazyAttribute(lambda o: faker.sentence(nb_words=4))
    about = factory.LazyAttribute(lambda o: faker.text())


class BlogFactory(factory.DjangoModelFactory):
    """Factory for blogs creating."""

    class Meta:
        model = Blog

    name = factory.LazyAttribute(lambda o: faker.sentence(nb_words=4))


class UserFactory(factory.DjangoModelFactory):
    """Factory for users creating."""

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.LazyAttribute(lambda o: faker.name())
    email = factory.LazyAttribute(lambda o: faker.email())
    password = factory.PostGenerationMethodCall('set_password',
                                                'default_password')
    profile = factory.RelatedFactory(UserProfileFactory, 'user')
    blogs = factory.RelatedFactory(BlogFactory, 'author')


class PostFactory(factory.DjangoModelFactory):
    """Factory for posts creating."""

    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda o: faker.sentence(nb_words=4))
    body = factory.LazyAttribute(lambda o: faker.text())
    blog = factory.SubFactory(BlogFactory)


class SubscriptionFactory(factory.DjangoModelFactory):
    """Factory for subscription creating."""

    class Meta:
        model = Subscription

    user = factory.SubFactory(UserFactory)
    blog = factory.SubFactory(BlogFactory)


class IsReadPostFactory(factory.DjangoModelFactory):
    """Factory for IsReadPost creating."""

    class Meta:
        model = IsReadPost

    subscription = factory.SubFactory(SubscriptionFactory)
    post = factory.SubFactory(PostFactory)
