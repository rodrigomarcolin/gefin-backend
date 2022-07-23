from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class BancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BancoModel
        fields = ['nome']
    
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['nome']

class ContaBancariaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContaBancariaModel
        fields = ['quantia', 'nome', 'desc', 'dono', 'banco']

class ControleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ControleModel
        fields = ['nome', 'desc', 'quantia', 'conta', 'data', 'gasto', 'tipoGasto', 'recorrente']

class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransacaoModel
        fields = ['quantia', 'nome', 'categoria', 'conta', 'pago_no_mes']