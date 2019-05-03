from django.urls import path
from agroaccount import views

urlpatterns = [
    path('agros/', views.AgroView.as_view(),name="agros"),
    # path('agros/<int:pk>/', views.agro_detail),
]