from django.urls import path

from . import views

urlpatterns = [
    path("<int:projeto_id>",views.projeto,name="index")
]