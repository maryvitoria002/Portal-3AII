from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def lista(request):
    """Página de materiais de estudo"""
    
    # Dados mock de materiais organizados por disciplina
    materiais = {
        'Matemática': [
            {
                'titulo': 'Apostila de Funções',
                'tipo': 'PDF',
                'tamanho': '2.5 MB',
                'data_upload': '25/09/2025',
                'downloads': 45,
                'icone': 'fas fa-file-pdf',
                'cor': '#ef4444'
            },
            {
                'titulo': 'Exercícios Resolvidos - Trigonometria',
                'tipo': 'PDF',
                'tamanho': '1.8 MB',
                'data_upload': '20/09/2025',
                'downloads': 32,
                'icone': 'fas fa-file-pdf',
                'cor': '#ef4444'
            }
        ],
        'Física': [
            {
                'titulo': 'Slides - Cinemática',
                'tipo': 'PPT',
                'tamanho': '5.2 MB',
                'data_upload': '22/09/2025',
                'downloads': 38,
                'icone': 'fas fa-file-powerpoint',
                'cor': '#f59e0b'
            }
        ],
        'História': [
            {
                'titulo': 'Resumo - Primeira Guerra Mundial',
                'tipo': 'PDF',
                'tamanho': '3.1 MB',
                'data_upload': '05/09/2025',
                'downloads': 35,
                'icone': 'fas fa-file-pdf',
                'cor': '#ef4444'
            }
        ]
    }
    
    # Estatísticas
    total_materiais = sum(len(disciplina) for disciplina in materiais.values())
    total_downloads = sum(
        sum(material['downloads'] for material in disciplina) 
        for disciplina in materiais.values()
    )
    
    estatisticas = {
        'total_materiais': total_materiais,
        'total_disciplinas': len(materiais),
        'total_downloads': total_downloads,
    }
    
    context = {
        'materiais': materiais,
        'estatisticas': estatisticas,
    }
    
    return render(request, 'materiais/lista.html', context)
