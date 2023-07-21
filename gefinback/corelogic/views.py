import datetime

from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.response import Response
from django.db.models.query import QuerySet

from .permissions import ContaBelongsToUser, IsAdminUserOrReadOnly, IsOwner
from .serializers import *


class BancoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bancos to be viewed or edited
    """
    serializer_class = BancoSerializer
    queryset = Banco.objects.all().order_by('nome')
    permission_classes = [IsAdminUserOrReadOnly]


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categorias to be viewed or edited
    """
    serializer_class = CategoriaTransacaoSerializer
    queryset = CategoriaTransacao.objects.all().order_by('nome')
    permission_classes = [IsAdminUserOrReadOnly]

#############################################
# Classes that deal with ContaBancariaModel #
#############################################


class ContaBancariaList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    """
        This view provides endpoints to
        list all conta bancarias and
        create a new conta bancaria
    """
    queryset = ContaBancaria.objects.all()
    serializer_class = ContaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Retorna apenas as contas do usuário que fez o get
    def get(self, request: HttpRequest, *args, **kwargs):
        contas = request.user.contas.all()
        serializer = self.serializer_class(contas, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # Popula campo de dono da conta como sendo o usuario do request
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

class ContaBancariaDetail(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

    queryset = ContaBancaria.objects.all()
    serializer_class = ContaBancariaSerializer
    """
        This class provides endpoints to
        retrieve, update and delete
        a given conta bancaria based on its id
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

####################################
# Classes that deal with Transacao #
####################################
class TransacaoList(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):

    """
        This class provides endpoints to
        create and retrieve transacoes
        related to an account
    """
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated, ContaBelongsToUser]

    # Executa antes de rodar o resto do código
    def setup(self, request, idconta, *args, **kwargs):
        # Seleciona conta cujo id está na URL
        self.conta = ContaBancaria.objects.filter(id=idconta).first()
        if self.conta is None:
            raise Http404
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        today = datetime.date.today()

        # se tem param all, retorna todos de qualquer mês
        if request.GET.get('all') is not None:
            transacs = Transacao.objects.filter(conta=self.conta)
        else:
            transacs = Transacao.objects.filter(
                conta=self.conta,
                data__month=today.month,
                data__year=today.year
            )

        serializer = self.serializer_class(transacs, many=True, context={'request':request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(conta=self.conta)

class TransacaoDetail(mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    """
        This class provides endpoints to
        detail, delete and update transacos
    """
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated, ContaBelongsToUser]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)