from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from .models import ContaBancariaModel

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
        try:
            dono = ContaBancariaModel.objects.filter(id=view.idconta).first().dono
        except:
            return False
        
        return dono == request.user