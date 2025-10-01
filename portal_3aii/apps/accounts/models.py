from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    turma = models.CharField(max_length=10, default='3AII')
    foto_perfil = models.ImageField(upload_to='perfis/', blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True)
    
    # Campos para controle
    is_lider = models.BooleanField(default=False, verbose_name='É líder da turma')
    data_criacao = models.DateTimeField(default=timezone.now)
    ultima_atividade = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo', 'matricula']
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f"{self.nome_completo} ({self.matricula})"
    
    def get_nome_curto(self):
        return self.nome_completo.split()[0] if self.nome_completo else self.username