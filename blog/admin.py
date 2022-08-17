from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Post
from .models import Imagens
from .models import Parceiros
    
# Register your models here.

class PostAdminForm(forms.ModelForm):
    imagens = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    def __init__(self, *args, **kwargs): 
        super(PostAdminForm, self).__init__(*args, **kwargs)
        self.fields['logo'].required = False
        self.fields['imagens'].required = False

class ImageAdminForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs): 
        super(ImageAdminForm, self).__init__(*args, **kwargs)            
        self.fields['img'] = forms.ImageField()
        self.fields['img'].required = False

class ImageInline(admin.TabularInline):
    model = Imagens
    extra = 1
    form = ImageAdminForm
    readonly_fields = ('img_preview',)

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Image Preview'
    img_preview.allow_tags = True

class PostAdmin(admin.ModelAdmin):
   search_fields = ['title']
   inlines = [ImageInline]
   form = PostAdminForm  
   readonly_fields = ('thumbnail_preview',)

   def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

   thumbnail_preview.short_description = 'Thumbnail Preview'
   thumbnail_preview.allow_tags = True

   def save_model(self, request, obj, form, change):
     obj.save()
     files = request.FILES.getlist('imagens')
     for f in files:
          x = Imagens.objects.create(post=obj,img=f)
          x.save()

admin.site.register(Parceiros)

admin.site.register(Post, PostAdmin)