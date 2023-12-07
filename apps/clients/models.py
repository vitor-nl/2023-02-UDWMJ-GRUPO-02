from django.db import models
from socialnetworks.models import Socialnetwork
from clientsocialnetworks import ClientSocialnetwork
class Cliente(models.Model):
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
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)
    redes_sociais = models.ManyToManyField(Socialnetwork, through=ClientSocialnetwork, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        app_label = 'clients'

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"
