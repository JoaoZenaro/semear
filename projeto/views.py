from django.shortcuts import render

from .models import Projeto

# Create your views here.

def projeto(request, projeto_id):
    projetos = Projeto.objects.all()
    projeto = Projeto.objects.get(pk=projeto_id)
    return render(request,'projeto/projeto.html', {
        'projeto': projeto,
        'projectList': projetos
    })