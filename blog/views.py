from django.shortcuts import render

from .models import Post

from projeto.models import Projeto

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    projetos = Projeto.objects.all()
    return render(request,'blog/index.html', {
        'posts': posts,
        'projectList': projetos
    })

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    projetos = Projeto.objects.all()
    return render(request,'blog/post.html', {
        'post': post,
        'projectList': projetos
    })