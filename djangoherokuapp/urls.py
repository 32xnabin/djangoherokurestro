
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from restroapi import views

urlpatterns = [
    
    #path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('admin/', admin.site.urls),
    path('', include('restroapi.urls')),
]
