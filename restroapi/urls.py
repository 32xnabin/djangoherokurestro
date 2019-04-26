from django.urls import path
from restroapi import views

urlpatterns = [
    path('restros/', views.restro_list),
    path('restros/<int:pk>/', views.restro_detail),
]