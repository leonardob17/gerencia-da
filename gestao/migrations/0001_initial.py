# Generated by Django 3.0.6 on 2020-06-01 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gestao.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=60)),
                ('ano_matricula', models.IntegerField(blank=True, null=True, verbose_name='Ano de Matrícula')),
                ('previsao_conclusao', models.IntegerField(blank=True, null=True, verbose_name='Previsão de Conclusão')),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('matricula', models.CharField(max_length=30, unique=True, verbose_name='Matrícula')),
                ('foto', models.ImageField(blank=True, null=True, upload_to=gestao.models.diretorio_usuario)),
                ('usuario_externo', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='O associado faz parte da chapa eleita?', verbose_name='É diretor?')),
                ('is_active', models.BooleanField(default=True, help_text='O associado ainda está estudado?', verbose_name='Aluno Ativo?')),
                ('is_external', models.BooleanField(default=False, help_text='Este usuário não é um associado do Diretório Acadêmico?', verbose_name='Usuário Externo?')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Associado',
                'verbose_name_plural': 'Associados',
            },
        ),
        migrations.CreateModel(
            name='DiretorioAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do diretório acadêmico')),
                ('sigla', models.CharField(default='', max_length=10, verbose_name='Sigla do diretório acadêmico')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Logo do diretório')),
            ],
            options={
                'verbose_name': 'Diretorio Acadêmico',
                'verbose_name_plural': 'Diretorio Acadêmico',
            },
        ),
        migrations.CreateModel(
            name='LinkCadastro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('validade', models.DateTimeField(default=gestao.models.mais_h)),
                ('tipo_usuario', models.PositiveIntegerField(choices=[(1, 'Diretor'), (2, 'Aluno'), (3, 'Egresso'), (4, 'Usuário Externo')])),
            ],
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data da reunião')),
                ('titulo', models.CharField(max_length=50, null=True, verbose_name='Título da Ata')),
                ('ata', models.TextField(verbose_name='Transcrição da ata...')),
                ('presentes', models.ManyToManyField(blank=True, related_name='reunioes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reunião',
                'verbose_name_plural': 'Reuniões',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('gestao.associado',),
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
            ],
            options={
                'verbose_name': 'Diretor',
                'verbose_name_plural': 'Diretores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('gestao.associado',),
        ),
        migrations.CreateModel(
            name='Egresso',
            fields=[
            ],
            options={
                'verbose_name': 'Egresso',
                'verbose_name_plural': 'Egressos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('gestao.associado',),
        ),
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
    ]
