from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.response import Response
from .permissions import IsOwner, IsAdminUserOrReadOnly, ContaBelongsToUser
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class BancoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bancos to be viewed or edited
    """
    serializer_class = BancoSerializer
    queryset = BancoModel.objects.all().order_by('nome')
    permission_classes = [IsAdminUserOrReadOnly]


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categorias to be viewed or edited
    """
    serializer_class = CategoriaSerializer
    queryset = CategoriaModel.objects.all().order_by('nome')
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
    queryset = ContaBancariaModel.objects.all()
    serializer_class = ContaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Retorna apenas as contas do usuário que fez o get
    def get(self, request, *args, **kwargs):
        if (request.user.is_anonymous):
            return HttpResponseForbidden()

        try:
            contas = ContaBancariaModel.objects.filter(dono=request.user)
        except ContaBancariaModel.DoesNotExist:
            raise Http404

        serializer = self.serializer_class(contas, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

class ContaBancariaDetail(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

    queryset = ContaBancariaModel.objects.all()
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
    queryset = TransacaoModel.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated, ContaBelongsToUser]

    def setup(self, request, idconta, *args, **kwargs):
        self.idconta = idconta
        try:
            self.conta = ContaBancariaModel.objects.filter(id=self.idconta).first()
        except ContaBancariaModel.DoesNotExist:
            raise Http404

        return super().setup(request, *args, **kwargs)

    # Retorna apenas as transações da conta que está sendo observada
    def get(self, request, *args, **kwargs):
        try:
            transacs = TransacaoModel.objects.filter(conta=self.conta)
        except TransacaoModel.DoesNotExist:
            raise Http404
        
        serializer = self.serializer_class(transacs, many=True, context={'request':request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(conta=self.conta)
