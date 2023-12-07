from .models import Cliente, Socialnetwork
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialnetwork
        fields = '__all__'