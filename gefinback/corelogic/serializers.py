from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'nome']
    
class CategoriaTransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaTransacao
        fields = ['id', 'nome']

class ContaBancariaSerializer(serializers.ModelSerializer):
    dono = serializers.ReadOnlyField(source='dono.username')
    class Meta:
        model = ContaBancaria
        fields = ['id', 'saldo', 'nome', 'desc', 'dono', 'banco']

class TransacaoSerializer(serializers.ModelSerializer):
    conta = serializers.ReadOnlyField(source="conta.id")
    class Meta:
        model = Transacao
        fields = ['id', 'quantia', 'nome', 'categoria', 'conta', 'data']
