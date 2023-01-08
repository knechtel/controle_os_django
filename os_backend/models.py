from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Equipment(models.Model):
    marca = models.TextField()
    modelo = models.TextField()
    serial = models.TextField()
    data_entrega = models.DateField(null=True)
    data_entrada = models.DateField(null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    nome = models.TextField()
    endereco = models.TextField()
    telefone = models.TextField()
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name="Equipment")
