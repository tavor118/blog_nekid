"""Urls for subscriptions application."""

from django.urls import path
from . import views


app_name = 'subscriptions'

urlpatterns = [
    path(
        'posts/',
        views.NewsFeedListView.as_view(),
        name='news_feed'
    ),
    path(
        'blogs/',
        views.SubscriptionListView.as_view(),
        name='index'
    ),
    path(
        'posts/<post_pk>/read',
        views.mark_as_read,
        name='mark_as_read'
    ),
]
