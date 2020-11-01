from django.shortcuts import render
from .data_access.ladies_repository import LadiesRepository
from .data_access.eventos_repository import EventosRepository
from .data_access.contato_repository import ContatoRepository
from .data_access.publicacao_repository import PublicacaoRepository
from .data_access.sobre_repository import SobreRepository

ladies_repository = LadiesRepository()

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def blog(request):
    return render(request, 'blog.html')

def eventos(request):
    return render(request, 'agenda.html')

def sobre(request):
    return render(request, 'sobrenos.html')

def ladies(request, id = None):
    '''
        View para obtenção dos dados das Ladies participantes
        do PyLadies Sergipe.
    '''
    context = {}

    if id:
        lady_obj = ladies_repository.get(query_params={'id':id})
        context['lady_obj'] = lady_obj
    
    ladies_list = ladies_repository.get_all().exclude(id=id)

    context['ladies_list'] = ladies_list

    return render(request, 'ladies.html', context)

def publicacao(request, slug=None):
    context = {
        'slug':slug,
        'id':1
    }
    return render(request, 'publicacao.html', context)