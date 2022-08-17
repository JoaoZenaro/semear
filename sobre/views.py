from django.shortcuts import render
from .models import Voluntario, Sobre

from projeto.models import Projeto

# Create your views here.
def index(request):
    voluntarios = Voluntario.objects.all()
    sobre = Sobre.objects.get(pk=1)
    projetos = Projeto.objects.all()
    return render(request,"sobre/index.html",{
        'voluntarios': voluntarios,
        'sobre': sobre,
        'projectList': projetos
    })