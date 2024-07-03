# multimedia/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_video, name='upload_video'),
    path('signup/', views.signup, name='signup'),
]

