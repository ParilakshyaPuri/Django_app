from django.urls import path
from . import views

urlpatterns = [
    path('central/', views.members, name='members'),
]