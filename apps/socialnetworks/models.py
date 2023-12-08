from django.db import models
from clients.models import Cliente 
from socialnetworks.models import Socialnetwork as SocialnetworkModel 

class Socialnetwork(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    redes_sociais = models.ManyToManyField(Cliente, through='clientsocialnetworks.ClientSocialnetwork', blank=True)
    
    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering = ['id']

    def __str__(self):
        return self.name
