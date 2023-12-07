from django.db import models
from clients.models import Cliente

class ConquistaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conquista_nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_conquista = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Conquista do Cliente'
        verbose_name_plural = 'Conquistas dos Clientes'
        ordering = ['-data_conquista']

    def __str__(self):
        return f"{self.cliente} - {self.conquista_nome}"