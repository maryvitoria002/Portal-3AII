from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
    
    def __str__(self):
        return self.titulo