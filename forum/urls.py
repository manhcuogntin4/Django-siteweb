from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='forum-home'),
    path(r'about/', views.about, name='forum-about'),
]