from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.farmer_login, name='farmer_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('add-farm/', views.add_farm, name='add_farm'),
    path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('agronomist-dashboard/', views.agronomist_dashboard, name='agronomist_dashboard'),
    path('extension-officer-dashboard/', views.admin_dashboard, name='extension_officer_dashboard'),
]