from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
