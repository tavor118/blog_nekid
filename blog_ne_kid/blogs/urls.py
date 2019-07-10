"""Urls for blogs application."""

from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path(
        '<blog_pk>/subscribe',
        views.subscribe_on_blog,
        name='subscribe'
    ),
    path(
        '<blog_pk>/unsubscribe',
        views.unsubscribe,
        name='unsubscribe'
    ),
    path(
        '<int:pk>/',
        views.PostListView.as_view(),
        name='post_list'
    ),
    path(
        '<int:pk>/posts/<post_pk>',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),

]
