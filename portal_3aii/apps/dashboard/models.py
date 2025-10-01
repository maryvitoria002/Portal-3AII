from django.db import models
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
