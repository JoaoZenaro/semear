from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Parceiros(models.Model):
     img = models.ImageField(
        upload_to = "media/",
        help_text= "Procure as imagens",
        null=True,
     )
     name = models.CharField(max_length=255)
     def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails')
    summary = RichTextField()
    body = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    logo = models.ManyToManyField(Parceiros, help_text="Selecione uma ou mais empresas parceiras")

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.title

    def display_logo(self):
        return ', '.join([logo.name for logo in self.logo.all()[:3]])

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return "" 

class Imagens(models.Model):
    img = models.ImageField(
        upload_to = "media/",
        help_text= "Procure as imagens",
        null=True,
    )
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, default=1)

    @property
    def img_preview(self):
        if self.img:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.img.url))
        return ""

