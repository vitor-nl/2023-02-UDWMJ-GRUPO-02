from django.db import models
from products.models import Product
from clients.models import Cliente

class OrderItem(models.Model):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preço = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product} - Price: {self.price}"
    
class Order(models.Model):
    corrida = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='orders')
    quantidade = models.IntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido para a corrida {self.corrida} - Status: {self.status} - Cliente: {self.cliente}"