from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def lista(request):
    """Página de professores da turma 3AII"""
    
    professores = [
        {
            'nome': 'Prof. Carlos Silva',
            'disciplina': 'Matemática',
            'email': 'carlos.silva@escola.com',
            'telefone': '(11) 98765-4321',
            'formacao': 'Licenciatura em Matemática - USP',
            'experiencia': '15 anos',
            'especializacao': 'Álgebra e Cálculo',
            'avatar': 'profile.svg',
            'cor': '#6366f1'
        },
        {
            'nome': 'Prof.ª Maria Santos',
            'disciplina': 'Português',
            'email': 'maria.santos@escola.com',
            'telefone': '(11) 98765-4322',
            'formacao': 'Letras - UNICAMP',
            'experiencia': '12 anos',
            'especializacao': 'Literatura Brasileira',
            'avatar': 'profile.svg',
            'cor': '#22c55e'
        },
        {
            'nome': 'Prof. João Oliveira',
            'disciplina': 'Física',
            'email': 'joao.oliveira@escola.com',
            'telefone': '(11) 98765-4323',
            'formacao': 'Física - ITA',
            'experiencia': '18 anos',
            'especializacao': 'Mecânica Quântica',
            'avatar': 'profile.svg',
            'cor': '#f59e0b'
        }
    ]
    
    context = {
        'professores': professores,
        'total_professores': len(professores)
    }
    
    return render(request, 'professores/lista.html', context)
