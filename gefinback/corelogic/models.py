from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BancoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class CategoriaModel(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class ContaBancariaModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512, blank=True, null=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')
    banco = models.ForeignKey(BancoModel, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.dono.__str__() + ": " + self.nome

class ControleModel(models.Model):
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512, blank=True, null=True)
    quantia = models.FloatField(default = 0)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    gasto = models.FloatField(default=0, blank=True, null=True)
    tipoGasto = models.BooleanField(default=True, blank=True, null=True)
    recorrente = models.BooleanField(default=False, blank=True, null=True)
 
    def __str__(self):
        return self.nome

class TransacaoModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, blank=True, null=True)
    controle = models.ForeignKey(ControleModel, on_delete=models.SET_NULL, blank=True, null=True)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.nome

class TransacaoRecorrenteModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, null=True)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    pago_no_mes = models.BooleanField()

    def __str__(self):
        return self.nome