from django.db import models
from django.contrib.auth import get_user_model
from apps.notas.models import Disciplina

User = get_user_model()

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    data_evento = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data_evento']
    
    def __str__(self):
        return self.titulo

class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_entrega = models.DateTimeField()
    concluida = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['data_entrega']
    
    def __str__(self):
        return self.titulo