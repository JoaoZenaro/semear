from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Voluntario(models.Model):
    nome = models.CharField(max_length=255)
    ocupacao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='voluntarios')

    def __str__(self):
        return self.nome

class Sobre(models.Model):
    body = RichTextUploadingField()
