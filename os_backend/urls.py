from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('v1/equipment/', views.EquipmentList.as_view(), name='list-equipment'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('v1/client/', views.ClientList.as_view(), name='list-client'),
    path('v1/client/new/', views.ClientCreate.as_view(), name='create-client'),
    path('v1/equipment/new/', views.EquipmentCreate.as_view(), name='list-equipment'),
]
