from django.shortcuts import render

from projeto.models import Projeto

# Create your views here.
def index(request):
    projetos = Projeto.objects.all()
    return render(request, "doacoes/index.html", {
        'projectList': projetos
    })