from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BancoViewSet(viewsets.ModelViewSet):
    serializer_class = BancoSerializer
    queryset = BancoModel.objects.all().order_by('nome')
    permission_classes = [permissions.IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = CategoriaModel.objects.all().order_by('nome')
    permission_classes = [permissions.IsAuthenticated]
