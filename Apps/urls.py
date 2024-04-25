
from django.contrib import admin
from django.urls import path

from .views import download_video

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', download_video, name='download_video'),
]
