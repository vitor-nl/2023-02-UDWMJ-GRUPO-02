from django.db import models
from django.test import Client
from apps import products
from categories.models import Category

# Create your models here.
class Product(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    distancia = models.FloatField()
    duracao = models.DurationField()
    data = models.DateField()
    ritmo = models.TimeField()
    condicoes_climaticas = models.CharField(max_length=100)
    terreno = models.CharField(max_length=100)
    observacoes = models.TextField()
    produtos = models.ManyToManyField(products, blank=True)

    def __str__(self):
        return f"Corrida de {self.cliente} em {self.data}"
