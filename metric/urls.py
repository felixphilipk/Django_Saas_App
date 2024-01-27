from django.contrib import admin
from django.urls import admin,path


urlpatterns = [
    path("polls/",include("polls.urls")),
    path("admin/",admin.site.url)
]