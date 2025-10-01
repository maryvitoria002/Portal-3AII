from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Aviso, Enquete
from datetime import timedelta
from django.http import HttpResponse

def home(request):
    # Avisos ativos
    try:
        avisos = Aviso.objects.filter(ativo=True)[:5]
    except:
        avisos = []
    
    # Enquetes ativas
    try:
        enquetes = Enquete.objects.filter(ativa=True)[:3]
    except:
        enquetes = []
    
    # Dados mockados para o dashboard funcionar
    tarefas_pendentes = [
        {'titulo': 'Trabalho de Matemática', 'disciplina': {'nome': 'Matemática', 'cor': '#007bff'}, 'data_entrega': timezone.now(), 'prioridade': 'alta'},
        {'titulo': 'Lista de Física', 'disciplina': {'nome': 'Física', 'cor': '#28a745'}, 'data_entrega': timezone.now(), 'prioridade': 'media'},
    ]
    
    proximos_eventos = [
        {'titulo': 'Prova de História', 'data_evento': timezone.now(), 'hora_inicio': '14:00', 'tipo': 'prova'},
        {'titulo': 'Apresentação Química', 'data_evento': timezone.now(), 'hora_inicio': '16:00', 'tipo': 'seminario'},
    ]
    
    ultimas_notas = [
        {'disciplina': {'nome': 'Português'}, 'nome_avaliacao': 'Redação', 'nota': 8.5},
        {'disciplina': {'nome': 'Inglês'}, 'nome_avaliacao': 'Prova oral', 'nota': 9.0},
    ]
    
    # Criar um usuário fake se não estiver logado
    usuario_fake = type('obj', (object,), {
        'get_nome_curto': lambda: 'Estudante 3AII',
        'matricula': '2024001',
        'is_authenticated': False,
        'foto_perfil': None
    })()
    
    context = {
        'avisos': avisos,
        'enquetes': enquetes,
        'tarefas_pendentes': tarefas_pendentes,
        'proximos_eventos': proximos_eventos,
        'ultimas_notas': ultimas_notas,
        'usuario': request.user if request.user.is_authenticated else usuario_fake
    }
    
    return render(request, 'dashboard/home.html', context)
