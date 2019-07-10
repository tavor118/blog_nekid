"""Module for interaction with an admin interface."""

from django.contrib import admin
from .models import Subscription, IsReadPost


admin.site.register(Subscription)
admin.site.register(IsReadPost)
