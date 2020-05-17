# Generated by Django 3.0.6 on 2020-05-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0014_auto_20200515_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Externo',
            fields=[
            ],
            options={
                'verbose_name': 'Usuário Externo',
                'verbose_name_plural': 'Usuários Externos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('gestao.associado',),
        ),
        migrations.AddField(
            model_name='associado',
            name='is_external',
            field=models.BooleanField(default=False, help_text='Este usuário não é um associado do Diretório Acadêmico?', verbose_name='Usuário Externo?'),
        ),
    ]