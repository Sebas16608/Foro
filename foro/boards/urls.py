from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [
    path('b/', views.random),
    path('m/', views.mierda)
]