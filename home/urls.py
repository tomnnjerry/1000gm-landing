from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('our-credentials/', views.credentials, name='credentials'),
    path('services/', views.services, name='services'),
    path('services/<str:pk>/', views.services_detail, name='services_detail'),
    
] 
