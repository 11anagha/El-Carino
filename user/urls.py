from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  
    path('logout/', views.user_logout, name='logout'), 
    path('services/', views.services, name='services'),
    path('plan/', views.plan_view, name='plan'),
]