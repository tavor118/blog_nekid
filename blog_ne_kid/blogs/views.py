"""Views for blogs application."""

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from subscriptions import services
from .models import Blog, Post


class BlogListView(generic.ListView):
    """View to display blogs."""
    queryset = Blog.objects.all().order_by("-created")
    template_name = 'blogs/index.html'


class PostListView(generic.ListView):
    """View to display posts."""
    model = Post
    context_object_name = 'post_list'
    template_name = 'blogs/post_list.html'

    def get_context_data(self, **kwargs):
        kwargs['blog'] = self.blog
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.blog = get_object_or_404(Blog, pk=self.kwargs.get('pk'))
        queryset = self.blog.posts.all()
        return queryset


class PostDetailView(generic.DetailView):
    """View to display detail information about post."""
    model = Post
    template_name = 'blogs/post_detail.html'


@login_required()
def subscribe_on_blog(request, blog_pk):
    """Subscribe on blog."""
    blog = get_object_or_404(Blog, pk=blog_pk)
    services.subscribe(blog, request.user)
    return redirect('blogs:post_list', pk=blog_pk)


@login_required()
def unsubscribe(request, blog_pk):
    """Unsubscribe from blog."""
    blog = get_object_or_404(Blog, pk=blog_pk)
    services.unsubscribe(blog, request.user)
    return redirect('subscriptions:index')
