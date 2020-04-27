# Generated by Django 3.0.5 on 2020-04-16 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financeiro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='associado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='venda',
            name='entrada_financeira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.EntradaFinanceira'),
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(through='financeiro.VendaProduto', to='financeiro.Produto'),
        ),
        migrations.AddField(
            model_name='transferenciafinanceira',
            name='carteira_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transferencias_para', to='financeiro.Carteira'),
        ),
        migrations.AddField(
            model_name='transferenciafinanceira',
            name='carteira_origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transferencias_de', to='financeiro.Carteira'),
        ),
        migrations.AddField(
            model_name='saidafinanceira',
            name='carteira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='financeiro.Carteira'),
        ),
        migrations.AddField(
            model_name='recibovenda',
            name='associado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recibovenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Venda'),
        ),
        migrations.AddField(
            model_name='entradafinanceira',
            name='carteira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='financeiro.Carteira'),
        ),
    ]
