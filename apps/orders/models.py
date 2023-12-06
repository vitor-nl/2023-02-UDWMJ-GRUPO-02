from django.db import models
from products.models import Product
from clients.models import Client

# Create your models here.
class Order(models.Model):
    corrida = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido para a corrida {self.corrida} - Status: {self.status}"