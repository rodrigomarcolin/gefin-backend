# Generated by Django 4.0.6 on 2022-07-26 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BancoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ContaBancariaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantia', models.FloatField(default=0)),
                ('nome', models.CharField(max_length=200)),
                ('desc', models.CharField(blank=True, max_length=512, null=True)),
                ('banco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corelogic.bancomodel')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ControleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('desc', models.CharField(blank=True, max_length=512, null=True)),
                ('quantia', models.FloatField(default=0)),
                ('data', models.DateField(auto_now_add=True)),
                ('gasto', models.FloatField(blank=True, default=0, null=True)),
                ('tipoGasto', models.BooleanField(blank=True, default=True, null=True)),
                ('recorrente', models.BooleanField(blank=True, default=False, null=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corelogic.contabancariamodel')),
            ],
        ),
        migrations.CreateModel(
            name='TransacaoRecorrenteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantia', models.FloatField(default=0)),
                ('nome', models.CharField(max_length=200)),
                ('pago_no_mes', models.BooleanField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='corelogic.categoriamodel')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corelogic.contabancariamodel')),
            ],
        ),
        migrations.CreateModel(
            name='TransacaoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantia', models.FloatField(default=0)),
                ('nome', models.CharField(max_length=200)),
                ('data', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corelogic.categoriamodel')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corelogic.contabancariamodel')),
                ('controle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corelogic.controlemodel')),
            ],
        ),
    ]