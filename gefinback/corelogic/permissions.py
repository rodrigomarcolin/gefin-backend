from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
        Permissão customizada que só permite que o dono de uma conta consiga
        acessar 
    """

    def has_object_permission(self, request, view, obj):
        return obj.dono == request.user