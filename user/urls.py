from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  
    path('logout/', views.user_logout, name='logout'), 
    path('services/', views.services, name='services'),
    path('plan/', views.plan_view, name='plan'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('wedding/', views.wedding, name='wedding'),
    path('tedx/', views.tedx, name='tedx'),
    path('mcd/', views.mcd, name='mcd'),
    path('contactus/', views.contactus, name='contactus'),
    path('blogd/', views.blogd, name='blogd'),
]