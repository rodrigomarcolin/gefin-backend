from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from .models import ContaBancaria

class IsOwner(permissions.BasePermission):
    """
        Permissão customizada que só permite que o dono de uma conta consiga
        acessar 
    """

    def has_object_permission(self, request, view, obj):
        return obj.dono == request.user


class IsAdminUserOrReadOnly(IsAdminUser):
    """
        Permite operação se o usuário for administrador ou 
        se a operação for segura
    """
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class ContaBelongsToUser(permissions.BasePermission):
    """
        Permite a operação se o usuário for dono da conta
    """
    def has_permission(self, request, view):
        conta = request.user.contas.filter(id=view.kwargs.get('idconta')).first()
        return conta is not None

    def has_object_permission(self, request, view, obj):
        conta = request.user.contas.filter(id=view.kwargs.get('idconta')).first()
        return conta is not None