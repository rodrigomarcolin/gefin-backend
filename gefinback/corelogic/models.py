from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Quanto um usuário é criado, gera um token para ele
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class BancoModel(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class CategoriaModel(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    
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

    class Meta:
        unique_together = [['dono', 'nome']]

class ObjetivoModel(models.Model):
    nome = models.CharField(max_length=200)
    desc = models.CharField(max_length=512, blank=True, null=True)
    quantia_meta = models.FloatField(default = 0)
    conta = models.ForeignKey(ContaBancariaModel, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    quantia_aplicada = models.FloatField(default=0, blank=True, null=True)    
    ultima_aplicacao = models.DateField(blank=True, null=True)
    prazo = models.DateField(blank=True, null=True)
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

    class Meta:
        unique_together = [['conta', 'nome']]

class TransacaoModel(models.Model):
    quantia = models.FloatField(default=0)
    nome = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, blank=True, null=True)
    objetivo = models.ForeignKey(ObjetivoModel, on_delete=models.SET_NULL, blank=True, null=True)
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