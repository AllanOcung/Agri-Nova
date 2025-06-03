# core app urls.py file

from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('load/<str:page>/', views.load_partial, name='load_partial'),
]
