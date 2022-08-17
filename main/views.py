from django.shortcuts import render

from blog.models import Post
from .models import Depoimentos

from projeto.models import Projeto

# Create your views here.
def index(request):
    depepoimento1 = Depoimentos.objects.all()[0]
    depoimentos = Depoimentos.objects.all().exclude(pk=depepoimento1.id)
    projetos = Projeto.objects.all()

    posts = Post.objects.all().order_by('-id')[:3]

    return render(request,'main/index.html', {
        'dep1': depepoimento1,
        'deps': depoimentos,
        'posts': posts,
        'projectList': projetos
    })