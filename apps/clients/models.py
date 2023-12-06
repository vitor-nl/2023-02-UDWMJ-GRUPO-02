from django.db import models
from socialnetworks.models import Product

# Create your models here.
class Client(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=100) 
    endereco = models.CharField(max_length=200)   
    numero_telefone = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    client_socialnetwork = models.ManyToManyField('Socialnetwork', through='ClientSocialnetwork', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_fabrication = models.DateField()
    is_active = models.BooleanField()
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    # ... outros campos do produto

    def __str__(self):
        return self.name
    