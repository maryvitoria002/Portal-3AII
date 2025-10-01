from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.CharField(max_length=200, help_text="Separadas por vírgula")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    sala = models.CharField(max_length=20, blank=True)
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
