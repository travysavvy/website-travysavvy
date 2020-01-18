from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
]