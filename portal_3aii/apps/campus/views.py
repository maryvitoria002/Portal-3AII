from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def vida_campus(request):
    """Página de vida no campus"""
    
    noticias = [
        {
            'titulo': 'Feira de Ciências 2025 é um Sucesso!',
            'resumo': 'Mais de 50 projetos foram apresentados pelos alunos do ensino médio.',
            'data': '28/09/2025',
            'categoria': 'Eventos',
            'cor': '#22c55e'
        },
        {
            'titulo': 'Nova Biblioteca Digital Disponível',
            'resumo': 'Acesso a milhares de livros e artigos científicos online.',
            'data': '25/09/2025',
            'categoria': 'Novidades',
            'cor': '#3b82f6'
        },
        {
            'titulo': 'Simulado ENEM - Resultados',
            'resumo': 'Parabéns a todos os participantes! Média geral: 750 pontos.',
            'data': '20/09/2025',
            'categoria': 'Resultados',
            'cor': '#8b5cf6'
        }
    ]
    
    eventos = [
        {
            'nome': 'Olimpíada de Matemática',
            'data': '15/10/2025',
            'horario': '14:00',
            'local': 'Auditório Principal',
            'tipo': 'Competição'
        },
        {
            'nome': 'Palestra sobre Sustentabilidade',
            'data': '22/10/2025',
            'horario': '16:00',
            'local': 'Sala de Conferências',
            'tipo': 'Palestra'
        }
    ]
    
    context = {
        'noticias': noticias,
        'eventos': eventos,
        'total_noticias': len(noticias),
        'total_eventos': len(eventos)
    }
    
    return render(request, 'campus/vida_campus.html', context)
