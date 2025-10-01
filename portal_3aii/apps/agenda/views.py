from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

def calendario(request):
    """Página de agenda e tarefas com sistema Kanban"""
    
    # Dados mock de tarefas para o Kanban
    todas_tarefas = [
        {
            'id': 1,
            'titulo': 'Trabalho de História',
            'materia': 'História',
            'descricao': 'Pesquisa sobre Revolução Industrial e suas consequências sociais',
            'prazo': datetime.now() + timedelta(days=2),
            'status': 'todo',
            'prioridade': 'alta',
            'cor': '#8b5cf6'
        },
        {
            'id': 2,
            'titulo': 'Lista de Matemática',
            'materia': 'Matemática',
            'descricao': 'Exercícios sobre função quadrática e parábolas',
            'prazo': datetime.now() + timedelta(days=5),
            'status': 'progress',
            'prioridade': 'media',
            'cor': '#6366f1'
        },
        {
            'id': 3,
            'titulo': 'Relatório de Física',
            'materia': 'Física',
            'descricao': 'Experimento sobre movimento retilíneo uniforme',
            'prazo': datetime.now() + timedelta(days=7),
            'status': 'todo',
            'prioridade': 'alta',
            'cor': '#f59e0b'
        },
        {
            'id': 4,
            'titulo': 'Redação Português',
            'materia': 'Português',
            'descricao': 'Dissertação argumentativa sobre sustentabilidade',
            'prazo': datetime.now() - timedelta(days=1),
            'status': 'done',
            'prioridade': 'alta',
            'cor': '#22c55e'
        },
        {
            'id': 5,
            'titulo': 'Exercícios de Química',
            'materia': 'Química',
            'descricao': 'Balanceamento de equações químicas',
            'prazo': datetime.now() + timedelta(days=3),
            'status': 'progress',
            'prioridade': 'media',
            'cor': '#3b82f6'
        },
        {
            'id': 6,
            'titulo': 'Apresentação Geografia',
            'materia': 'Geografia',
            'descricao': 'Biomas brasileiros e conservação ambiental',
            'prazo': datetime.now() + timedelta(days=8),
            'status': 'todo',
            'prioridade': 'baixa',
            'cor': '#06b6d4'
        },
        {
            'id': 7,
            'titulo': 'Resumo de Biologia',
            'materia': 'Biologia',
            'descricao': 'Sistema cardiovascular humano',
            'prazo': datetime.now() - timedelta(days=2),
            'status': 'done',
            'prioridade': 'media',
            'cor': '#10b981'
        }
    ]
    
    # Organizar tarefas por status para o Kanban
    tarefas_a_fazer = [t for t in todas_tarefas if t['status'] == 'todo']
    tarefas_em_progresso = [t for t in todas_tarefas if t['status'] == 'progress']
    tarefas_concluidas = [t for t in todas_tarefas if t['status'] == 'done']
    
    # Eventos do calendário
    eventos = [
        {
            'titulo': 'Prova de Matemática',
            'data': datetime.now() + timedelta(days=3),
            'tipo': 'prova',
            'disciplina': 'Matemática',
            'cor': '#6366f1'
        },
        {
            'titulo': 'Feira de Ciências',
            'data': datetime.now() + timedelta(days=15),
            'tipo': 'evento',
            'disciplina': 'Geral',
            'cor': '#22c55e'
        },
        {
            'titulo': 'Simulado ENEM',
            'data': datetime.now() + timedelta(days=25),
            'tipo': 'simulado',
            'disciplina': 'Geral',
            'cor': '#8b5cf6'
        }
    ]
    
    # Estatísticas
    estatisticas = {
        'total_tarefas': len(todas_tarefas),
        'tarefas_pendentes': len(tarefas_a_fazer) + len(tarefas_em_progresso),
        'tarefas_concluidas': len(tarefas_concluidas),
        'proximos_eventos': len(eventos)
    }
    
    context = {
        'todas_tarefas': todas_tarefas,
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_em_progresso': tarefas_em_progresso,
        'tarefas_concluidas': tarefas_concluidas,
        'eventos': eventos,
        'estatisticas': estatisticas,
    }
    
    return render(request, 'agenda/calendario.html', context)