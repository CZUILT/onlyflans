# carpeta urls.py creada manualmente en app web

from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name="home"), 
    path('about', views.about, name="acerca"),
    path('welcome', views.welcome, name="bienvenido"),
    path('nueva', views.nueva_vista),
    path('contacto', views.contacto, name="contacto"),
    path('exito',views.exito, name="exito"),
]