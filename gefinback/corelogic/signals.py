"""
Funções que lidam com eventos dos objetos
"""
from django.db.models.signals import pre_save, post_delete
from .models import Transacao, ContaBancaria
from django.dispatch import receiver

@receiver(pre_save, sender=Transacao)
def on_save_transacao(sender: Transacao, **kwargs):
    instance: Transacao = kwargs['instance']
    
    old_transacao = Transacao.objects.filter(id=instance.id).first()
    old_transacao_quantia = 0 if old_transacao is None else old_transacao.quantia

    conta = instance.conta
    conta.saldo = conta.saldo - old_transacao_quantia + instance.quantia
    conta.save()

@receiver(post_delete)
def on_delete_transacao(sender: Transacao, **kwargs):
    instance: Transacao = kwargs['instance']
    conta = instance.conta
    conta.saldo -= instance.quantia
    conta.save()
