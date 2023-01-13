from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from os_backend.serializers import ClientSeriliazers, EquipmentSeriliazers
from .models import Client, Equipment
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.
#@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
class EquipmentList(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSeriliazers


#@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class EquipmentCreate(CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSeriliazers


@permission_classes([IsAuthenticated])
class ClientCreate(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSeriliazers


@permission_classes([IsAuthenticated])
class ClientList(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSeriliazers
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
