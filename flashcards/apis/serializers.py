from .models import *
from rest_framework import serializers


class SlowaSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True)
    dislikes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Slowa
        fields = ('id_slowo', 'autor', 'data_dod', 'slowo', 'sumalike', 'likes', 'dislikes')

class DefinicjeSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True)
    dislikes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Definicje
        fields = ('id_slowo', 'id_definicja', 'autor', 'data_dod', 'definicja', 'sumalike', 'likes', 'dislikes')
