
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("shorten", views.shorten, name="shorten"),
    path("<str:short_url>", views.shorten_url, name="shorten_url"),
    path("analytics/<str:short_url>", views.analytics_view, name="analytics"),
    path("html/url", views.list_url, name="list_url"),
    path("json/url", views.json_url, name="json_url"),
]
