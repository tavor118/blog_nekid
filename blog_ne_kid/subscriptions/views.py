"""Views for subscription application."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blogs.models import Post
from .models import Subscription
from . import services


class SubscriptionListView(LoginRequiredMixin, generic.ListView):
    """View to display subscribed blogs."""
    template_name = 'subscriptions/index.html'

    def get_queryset(self):
        return Subscription.objects \
            .filter(user=self.request.user) \
            .select_related('blog')


class NewsFeedListView(LoginRequiredMixin, generic.ListView):
    """View to display feed news."""
    template_name = 'subscriptions/news_feed.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        kwargs['read_post_list'] = Post.objects.filter(
            read_posts__subscription__user=self.request.user
        )
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Post.objects \
            .filter(blog__subscriptions__user=self.request.user) \
            .order_by('-created')


@login_required()
def mark_as_read(request, post_pk):
    """Mark post as read in feed news."""
    post = get_object_or_404(Post, pk=post_pk)
    subscription = Subscription.objects \
        .filter(user=request.user) \
        .filter(blog=post.blog).first()
    services.mark_as_read(post, subscription)
    return redirect('subscriptions:news_feed')
