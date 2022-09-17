from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.BancoModel)
admin.site.register(models.CategoriaModel)

# Customizing admin
admin.site.site_header = "Painel do Administrador do Gefin"