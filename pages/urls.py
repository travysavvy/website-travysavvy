from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('about/', views.about),
    path('news/', views.news),
]