from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from os_backend.models import Client, Equipment
from django.db import models


class ClientSeriliazers(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EquipmentSeriliazers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
