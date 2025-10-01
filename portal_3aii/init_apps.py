#!/usr/bin/env python
"""
Script de inicialização do Portal 3AII
Este script cria todas as apps necessárias e seus arquivos básicos
"""

import os
import sys

def create_app_files(app_name, models_content="", views_content="", urls_content="", admin_content=""):
    """Cria os arquivos básicos de uma app Django"""
    
    # Criar diretório da app
    app_dir = f"apps/{app_name}"
    os.makedirs(app_dir, exist_ok=True)
    
    # __init__.py
    with open(f"{app_dir}/__init__.py", "w") as f:
        f.write("")
    
    # apps.py
    apps_content = f"""from django.apps import AppConfig


class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app_name}'
    verbose_name = '{app_name.capitalize()}'
"""
    with open(f"{app_dir}/apps.py", "w") as f:
        f.write(apps_content)
    
    # models.py
    if not models_content:
        models_content = """from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Adicione seus models aqui
"""
    with open(f"{app_dir}/models.py", "w") as f:
        f.write(models_content)
    
    # views.py
    if not views_content:
        views_content = """from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Adicione suas views aqui
"""
    with open(f"{app_dir}/views.py", "w") as f:
        f.write(views_content)
    
    # urls.py
    if not urls_content:
        urls_content = f"""from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    # Adicione suas URLs aqui
]
"""
    with open(f"{app_dir}/urls.py", "w") as f:
        f.write(urls_content)
    
    # admin.py
    if not admin_content:
        admin_content = """from django.contrib import admin
from .models import *

# Registre seus models aqui
"""
    with open(f"{app_dir}/admin.py", "w") as f:
        f.write(admin_content)
    
    print(f"✓ App '{app_name}' criada com sucesso!")

def create_all_apps():
    """Cria todas as apps do projeto"""
    
    print("🚀 Criando estrutura completa do Portal 3AII...")
    print("=" * 50)
    
    # App Dashboard (já existe, vamos completar)
    dashboard_models = """from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Aviso(models.Model):
    TIPOS_AVISO = [
        ('info', 'Informação'),
        ('urgente', 'Urgente'),
        ('evento', 'Evento'),
        ('prova', 'Prova'),
        ('trabalho', 'Trabalho'),
    ]
    
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS_AVISO, default='info')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_expiracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    fixado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
        ordering = ['-fixado', '-data_criacao']
    
    def __str__(self):
        return self.titulo

class Enquete(models.Model):
    pergunta = models.CharField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_expiracao = models.DateTimeField()
    ativa = models.BooleanField(default=True)
    multipla_escolha = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.pergunta

class OpcaoEnquete(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, related_name='opcoes')
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.enquete.pergunta} - {self.texto}"
"""
    
    dashboard_views = """from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Aviso, Enquete
from datetime import timedelta

@login_required
def home(request):
    # Avisos ativos
    avisos = Aviso.objects.filter(ativo=True)[:5]
    
    # Enquetes ativas
    enquetes = Enquete.objects.filter(ativa=True)[:3]
    
    context = {
        'avisos': avisos,
        'enquetes': enquetes,
        'usuario': request.user
    }
    
    return render(request, 'dashboard/home.html', context)
"""
    
    create_app_files('dashboard', dashboard_models, dashboard_views)
    
    # App Materiais
    materiais_models = """from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cor = models.CharField(max_length=7, default='#007bff')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome

class Material(models.Model):
    TIPOS_MATERIAL = [
        ('pdf', 'PDF'),
        ('slide', 'Slide/Apresentação'),
        ('video', 'Vídeo'),
        ('link', 'Link'),
        ('codigo', 'Código'),
        ('exercicio', 'Exercício'),
        ('prova', 'Prova Anterior'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS_MATERIAL)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='materiais/', blank=True, null=True)
    link = models.URLField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.CharField(max_length=100, blank=True)
    data_upload = models.DateTimeField(default=timezone.now)
    downloads = models.IntegerField(default=0)
    publico = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Separadas por vírgula")
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering = ['-data_upload']
    
    def __str__(self):
        return self.titulo
"""
    
    create_app_files('materiais', materiais_models)
    
    # App Professores
    professores_models = """from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.CharField(max_length=200, help_text="Separadas por vírgula")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    sala = models.CharField(max_length=20, blank=True)
    horario_atendimento = models.TextField(blank=True)
    metodo_avaliativo = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    foto = models.ImageField(upload_to='professores/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Monitoria(models.Model):
    DIAS_SEMANA = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    ]
    
    disciplina = models.CharField(max_length=100)
    monitor = models.CharField(max_length=100)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20, choices=DIAS_SEMANA)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    local = models.CharField(max_length=100)
    contato_monitor = models.CharField(max_length=100, blank=True)
    ativa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Monitoria'
        verbose_name_plural = 'Monitorias'
        ordering = ['dia_semana', 'horario_inicio']
    
    def __str__(self):
        return f"{self.disciplina} - {self.monitor}"
"""
    
    create_app_files('professores', professores_models)
    
    # App Campus
    campus_models = """from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class HorarioAula(models.Model):
    DIAS_SEMANA = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    ]
    
    disciplina = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    dia_semana = models.CharField(max_length=20, choices=DIAS_SEMANA)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    sala = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Horário de Aula'
        verbose_name_plural = 'Horários de Aulas'
        ordering = ['dia_semana', 'horario_inicio']
    
    def __str__(self):
        return f"{self.disciplina} - {self.get_dia_semana_display()}"

class AchadoPerdido(models.Model):
    STATUS_CHOICES = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('devolvido', 'Devolvido'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    local_encontrado = models.CharField(max_length=100, blank=True)
    data_ocorrencia = models.DateField()
    foto = models.ImageField(upload_to='achados_perdidos/', blank=True, null=True)
    contato = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(default=timezone.now)
    resolvido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Achado e Perdido'
        verbose_name_plural = 'Achados e Perdidos'
        ordering = ['-data_publicacao']
    
    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"
"""
    
    create_app_files('campus', campus_models)
    
    print("\n🎉 Estrutura completa criada com sucesso!")
    print("\nPróximos passos:")
    print("1. Execute: python manage.py makemigrations")
    print("2. Execute: python manage.py migrate")
    print("3. Execute: python manage.py createsuperuser")
    print("4. Execute: python manage.py runserver")

if __name__ == "__main__":
    create_all_apps()