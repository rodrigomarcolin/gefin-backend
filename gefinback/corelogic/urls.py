"""gefinback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'banco', views.BancoViewSet)
router.register(r'categoria', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contabanc/', views.ContaBancariaList.as_view()),
    path('contabanc/<int:pk>', views.ContaBancariaDetail.as_view()),
    path('contabanc/<int:idconta>/transac', views.TransacaoList.as_view()),
    path('contabanc/<int:idconta>/transac/<int:pk>', views.TransacaoDetail.as_view()),
    path('contabanc/<int:idconta>/transac_reco', views.TransacaoRecorrenteList.as_view()),
    path('contabanc/<int:idconta>/transac_reco/<int:pk>', views.TransacaoRecorrenteDetail.as_view()),
    path('contabanc/<int:idconta>/objetivo', views.ObjetivoList.as_view()),
    path('contabanc/<int:idconta>/objetivo/<int:pk>', views.ObjetivoDetail.as_view()),
]