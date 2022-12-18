from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.index, name ='index'),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
    
    path('landing/', views.index),
    path('contact/', views.contact),
    path('services/', views.services),
    path('aboutus/', views.about),
    path('serviceform/', views.serviceform),
    path('donation/', views.donation),    

]