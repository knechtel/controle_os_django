from django.shortcuts import render
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from rest_framework.generics import ListAPIView, CreateAPIView


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Client, Equipment
from os_backend.serializers import ClientSeriliazers, EquipmentSeriliazers


# Create your views here.
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
class EquipmentList(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSeriliazers


# @authentication_classes([SessionAuthentication, BasicAuthentication])
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
