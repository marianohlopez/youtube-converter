from django.urls import path
from . import views

urlpatterns = [
    path('audio', views.download_audio, name='convert_audio'),
    path('video', views.download_video, name='convert_video'),
]
