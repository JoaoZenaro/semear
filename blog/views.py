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

    blog_object = Post.objects.get(id=post_id)
    blog_object.views = blog_object.views+1
    blog_object.save()

    return render(request,'blog/post.html', {
        'post': post,
        'projectList': projetos
    })