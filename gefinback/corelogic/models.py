from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Banco(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class CategoriaTransacao(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class ContaBancaria(models.Model):
    saldo = models.FloatField(default=0, verbose_name="Saldo")
    nome = models.CharField(max_length=200, verbose_name="Nome da Conta")
    desc = models.CharField(max_length=512, blank=True, null=True, verbose_name="Descrição")
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')
    banco = models.ForeignKey(Banco, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.dono.__str__() + ": " + self.nome

    class Meta:
        unique_together = [['dono', 'nome']]


class Transacao(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaTransacao, on_delete=models.SET_NULL, blank=True, null=True)
    conta = models.ForeignKey(ContaBancaria, on_delete=models.CASCADE, related_name='transacoes')
   
    def __str__(self):
        return self.nome