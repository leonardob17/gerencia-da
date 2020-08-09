# Generated by Django 3.0.7 on 2020-06-11 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkcadastro',
            name='reutilizavel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data da reunião'),
        ),
    ]