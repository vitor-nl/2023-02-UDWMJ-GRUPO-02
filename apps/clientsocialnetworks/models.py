from django.db import models
from clients.models import Cliente
from socialnetworks.models import Socialnetwork

class ClientSocialnetwork(models.Model):
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(Socialnetwork, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, help_text="Nome de usuário na rede social")
    follower_count = models.PositiveIntegerField(help_text="Número de seguidores na rede social", null=True, blank=True)
    race_results = models.TextField(help_text="Resultados de corridas compartilhados na rede social", null=True, blank=True)
    
    class Meta:
        unique_together = ('client', 'socialnetwork')