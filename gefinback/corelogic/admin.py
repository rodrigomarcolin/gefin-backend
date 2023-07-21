from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Banco)
admin.site.register(models.CategoriaTransacao)

# Customizing admin
admin.site.site_header = "Painel do Administrador do Gefin"