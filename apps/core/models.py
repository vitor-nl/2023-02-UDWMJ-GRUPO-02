from django.db import models
from django.test import Client

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Conquista(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Categoria: {self.categoria}"

class ConquistaClient(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} - {self.conquista}"