from django.db import models
from categories.models import Category
from clients.models import Cliente

class Product(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    distancia = models.FloatField()
    duracao = models.DurationField()
    data = models.DateField()
    ritmo = models.TimeField()
    condicoes_climaticas = models.CharField(max_length=100)
    terreno = models.CharField(max_length=100)
    observacoes = models.TextField()
    produtos = models.ManyToManyField('self', blank=True)  

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']

    def __str__(self):
        return f"Corrida de {self.cliente} em {self.data}"