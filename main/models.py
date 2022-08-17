from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Depoimentos(models.Model):
    body = RichTextField()
    imagem = models.ImageField(upload_to='depoimentos')
