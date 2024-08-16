# carpeta urls.py creada manualmente en app web

from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('about/', views.acerca), 
    path('welcome/', views.bienvenido),
]