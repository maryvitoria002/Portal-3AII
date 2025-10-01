from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HorarioAula(models.Model):
    disciplina = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    sala = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Horário de Aula'
        verbose_name_plural = 'Horários de Aulas'
    
    def __str__(self):
        return f"{self.disciplina} - {self.professor}"
