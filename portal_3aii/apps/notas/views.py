from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def boletim(request):
    """Página de boletim com notas e médias"""
    
    # Dados mock das disciplinas e notas
    disciplinas = [
        {
            'nome': 'Matemática',
            'professor': 'Prof. Carlos Silva',
            'notas': [8.5, 7.8, 9.2, 8.0],
            'media': 8.4,
            'situacao': 'aprovado',
            'cor': '#6366f1'
        },
        {
            'nome': 'Português',
            'professor': 'Prof.ª Maria Santos',
            'notas': [9.0, 8.5, 8.8, 9.2],
            'media': 8.9,
            'situacao': 'aprovado',
            'cor': '#22c55e'
        },
        {
            'nome': 'Física',
            'professor': 'Prof. João Oliveira',
            'notas': [7.5, 6.8, 8.0, 7.2],
            'media': 7.4,
            'situacao': 'aprovado',
            'cor': '#f59e0b'
        },
        {
            'nome': 'Química',
            'professor': 'Prof.ª Ana Costa',
            'notas': [8.0, 7.5, 8.5, 8.2],
            'media': 8.1,
            'situacao': 'aprovado',
            'cor': '#3b82f6'
        },
        {
            'nome': 'História',
            'professor': 'Prof. Pedro Lima',
            'notas': [9.5, 8.8, 9.0, 9.2],
            'media': 9.1,
            'situacao': 'aprovado',
            'cor': '#8b5cf6'
        },
        {
            'nome': 'Geografia',
            'professor': 'Prof.ª Laura Rocha',
            'notas': [8.2, 7.9, 8.5, 8.0],
            'media': 8.2,
            'situacao': 'aprovado',
            'cor': '#06b6d4'
        }
    ]
    
    # Estatísticas gerais
    estatisticas = {
        'media_geral': 8.3,
        'total_disciplinas': len(disciplinas),
        'disciplinas_aprovado': len([d for d in disciplinas if d['situacao'] == 'aprovado']),
        'melhor_disciplina': max(disciplinas, key=lambda x: x['media']),
        'frequencia': 95.5
    }
    
    context = {
        'disciplinas': disciplinas,
        'estatisticas': estatisticas,
    }
    
    return render(request, 'notas/boletim.html', context)