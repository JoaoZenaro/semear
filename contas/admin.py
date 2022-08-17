from django.contrib import admin
from .models import Conta
from django import forms
from .models import Imagens

# Register your models here.

class ContaAdminForm(forms.ModelForm):
    imagens = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    def __init__(self, *args, **kwargs): 
        super(ContaAdminForm, self).__init__(*args, **kwargs)
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

class ContaAdmin(admin.ModelAdmin):
   search_fields = ['title']
   inlines = [ImageInline]
   form = ContaAdminForm  

   def save_model(self, request, obj, form, change):
     obj.save()
     files = request.FILES.getlist('imagens')
     for f in files:
          x = Imagens.objects.create(conta=obj,img=f)
          x.save()

admin.site.register(Conta, ContaAdmin)