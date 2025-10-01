from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'nome_completo', 'matricula', 'email', 'is_lider', 'date_joined')
    list_filter = ('is_lider', 'turma', 'date_joined')
    search_fields = ('username', 'nome_completo', 'matricula', 'email')
    readonly_fields = ('date_joined', 'last_login', 'data_criacao', 'ultima_atividade')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'email', 'matricula', 'turma', 'telefone', 'data_nascimento', 'endereco', 'foto_perfil')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_lider', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined', 'data_criacao', 'ultima_atividade')}),
    )