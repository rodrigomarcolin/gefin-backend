"""
Funções que lidam com eventos dos objetos
"""
from django.db.models.signals import pre_save, post_delete
from .models import Transacao, ContaBancaria
from django.dispatch import receiver

@receiver(post_delete)
def on_delete_transacao(sender: Transacao, **kwargs):
    instance: Transacao = kwargs['instance']
    conta = instance.conta
    conta.saldo -= instance.quantia
    conta.save()
