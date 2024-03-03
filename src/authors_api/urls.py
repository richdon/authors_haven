from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("supersecret/", admin.site.urls),
]
