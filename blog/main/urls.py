from django.urls import path
from main import views

urlpatterns = [
    path('', views.main),  # главная /
    path('about/', views.about),  # /about
    path('contacts/', views.contacts),
    path('text/', views.text),
    
]