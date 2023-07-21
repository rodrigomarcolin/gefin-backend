from django.contrib import admin
from . import models

# Register your models here.

admin.site.register([models.Banco, models.CategoriaTransacao, models.Transacao, models.ContaBancaria])
# Customizing admin
admin.site.site_header = "Painel do Administrador do Gefin"