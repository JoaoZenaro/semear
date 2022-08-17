from django.shortcuts import render
from .models import Conta

from projeto.models import Projeto

# Create your views here.
def index(request):
    conta = Conta.objects.all().order_by('-created_at')
    projetos = Projeto.objects.all()
    return render(request,'contas/index.html', {
        'conta': conta,
        'projectList': projetos
    })

def conta(request, conta_id):
    conta = Conta.objects.get(pk=conta_id)
    projetos = Projeto.objects.all()
    return render(request,'contas/conta.html', {
        'conta': conta,
        'projectList': projetos
    })