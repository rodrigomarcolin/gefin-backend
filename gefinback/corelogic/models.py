from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BancoModel(models.Model):
    nome = models.CharField(max_length=200)

class CategoriaModel(models.Model):
    nome = models.CharField(max_length=200)

class ContaBancariaModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.ForeignKey(BancoModel, on_delete=models.SET_NULL, blank=True, null=True)

class ControleModel(models.Model):
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512)
    quantia = models.FloatField(default = 0)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    gasto = models.FloatField(default=0)
    tipoGasto = models.BooleanField()
    recorrente = models.BooleanField()

class TransacaoModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, blank=True, null=True)
    controle = models.ForeignKey(ControleModel, on_delete=models.SET_NULL, blank=True, null=True)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)

class TransacaoRecorrenteModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, null=True)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    pago_no_mes = models.BooleanField()