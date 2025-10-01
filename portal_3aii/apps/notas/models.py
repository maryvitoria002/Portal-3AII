from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    professor = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome_avaliacao = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
    
    def __str__(self):
        return f"{self.disciplina.nome} - {self.nome_avaliacao}: {self.nota}"