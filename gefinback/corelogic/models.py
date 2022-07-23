from importlib.metadata import requires
from pyexpat import model
from turtle import ondrag
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ContaBancariaModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512)
    dono = models.ForeignKey
    banco = models.ForeignKey(BancoModel, on_delete=models.SET_NULL, blank=True)


class BancoModel(models.Model):
    nome = models.CharField(max_length=200)

class CategoriaModel(models.Model):
    nome = models.CharField(max_length=200)

class ControleModel(models.Model):
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512)
    quantia = models.FloatField(default = 0)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    mes = models.DateField(auto_now=True, auto_now_add=True)
    tipoGasto = models.BooleanField()

class TransacaoModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    data = models.DateField(auto_now=True, auto_now_add=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, blank=True)
    controle = models.ForeignKey(ControleModel, on_delete=models.SET_NULL, blank=True)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)

class TransacaoRecorrente(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)

