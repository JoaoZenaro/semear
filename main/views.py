from django.shortcuts import render

from blog.models import Post
from .models import Depoimentos

from projeto.models import Projeto

# Create your views here.
def index(request):

    depepoimento1 = Depoimentos.objects.first()
    depoimentos = Depoimentos.objects.exclude(pk=depepoimento1.pk) if depepoimento1 else []
    projetos = Projeto.objects.all()
    posts = Post.objects.order_by('-id')[:3] if Post.objects.exists() else []

    return render(request,'main/index.html', {
        'dep1': depepoimento1,
        'deps': depoimentos,
        'posts': posts,
        'projectList': projetos
    })