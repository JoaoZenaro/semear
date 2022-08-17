from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from PIL import Image

# Create your models here.
class Conta(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.title

class Imagens(models.Model):
    img = models.ImageField(
        upload_to = "media/",
        help_text= "Procure as imagens",
        null=True,
    )
    conta = models.ForeignKey(
        "Conta", on_delete=models.CASCADE, default=1)
        
    @property
    def img_preview(self):
        if self.img:
            return mark_safe('<img src="{}" width="300" height="300" style="object-fit: cover;" />'.format(self.img.url))
        return ""

 