from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    contas = serializers.PrimaryKeyRelatedField(many=True, queryset=ContaBancariaModel.objects.all())
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'contas']

class BancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BancoModel
        fields = ['id', 'nome']
    
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['id', 'nome']

class ContaBancariaSerializer(serializers.HyperlinkedModelSerializer):
    dono = serializers.ReadOnlyField(source='dono.username')
    class Meta:
        model = ContaBancariaModel
        fields = ['id', 'quantia', 'nome', 'desc', 'dono', 'banco']

class ControleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ControleModel
        fields = ['id', 'nome', 'desc', 'quantia', 'conta', 'data', 'gasto', 'tipoGasto', 'recorrente']

class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransacaoModel
        fields = ['id', 'quantia', 'nome', 'categoria', 'conta', 'pago_no_mes']