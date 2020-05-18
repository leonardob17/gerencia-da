# Generated by Django 3.0.6 on 2020-05-18 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaFinanceira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('servico', models.BooleanField(default=False)),
                ('arquivado', models.BooleanField(default=False)),
                ('foto', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ReciboVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaidaFinanceira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransferenciaFinanceira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desconto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VendaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('desconto', models.IntegerField(default=0)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='financeiro.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Venda')),
            ],
        ),
    ]
