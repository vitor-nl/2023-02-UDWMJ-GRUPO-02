from rest_framework import serializers
from .models import ClientSocialnetwork

class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialnetwork
        fields = '__all__'
