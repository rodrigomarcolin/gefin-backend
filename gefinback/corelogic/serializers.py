from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    contas = serializers.PrimaryKeyRelatedField(many=True, queryset=ContaBancariaModel.objects.all())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'contas']

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoModel
        fields = ['id', 'nome']
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['id', 'nome']

class ContaBancariaSerializer(serializers.ModelSerializer):
    dono = serializers.ReadOnlyField(source='dono.username')
    class Meta:
        model = ContaBancariaModel
        fields = ['id', 'quantia', 'nome', 'desc', 'dono', 'banco']

class ControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleModel
        fields = ['id', 'nome', 'desc', 'quantia', 'conta', 'data', 'gasto', 'tipoGasto', 'recorrente']

class TransacaoSerializer(serializers.ModelSerializer):
    conta = serializers.ReadOnlyField(source="conta.id")
    class Meta:
        model = TransacaoModel
        fields = ['id', 'quantia', 'nome', 'categoria', 'controle', 'conta']