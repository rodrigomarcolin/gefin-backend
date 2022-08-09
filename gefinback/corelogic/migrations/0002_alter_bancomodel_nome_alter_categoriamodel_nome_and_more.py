# Generated by Django 4.0.6 on 2022-07-27 04:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('corelogic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancomodel',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='categoriamodel',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='contabancariamodel',
            unique_together={('dono', 'nome')},
        ),
        migrations.AlterUniqueTogether(
            name='controlemodel',
            unique_together={('conta', 'nome')},
        ),
    ]
