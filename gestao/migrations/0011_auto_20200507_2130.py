# Generated by Django 3.0.6 on 2020-05-07 21:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0010_auto_20200504_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='reuniao',
            name='titulo',
            field=models.CharField(max_length=50, null=True, verbose_name='Título da Ata'),
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='data',
            field=models.DateField(verbose_name='Data da reunião'),
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='presentes',
            field=models.ManyToManyField(related_name='reunioes', to=settings.AUTH_USER_MODEL),
        ),
    ]