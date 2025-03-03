from django.urls import path
from django.http import HttpResponse
from Hotel import views

urlpatterns = [
    path('home/', views.home, name='home'),
    
]
    