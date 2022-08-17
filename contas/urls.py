from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('<int:conta_id>',views.conta)
]