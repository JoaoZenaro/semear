from django.contrib import admin
from django import forms
from .models import Voluntario, Sobre

# Register your models here.

admin.site.register(Voluntario)
admin.site.register(Sobre)