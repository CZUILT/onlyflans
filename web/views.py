from django.shortcuts import render
from.models import Flan

def home(req):
        # flanes_all = Flan.objects.all() 
        flanes_publicos = Flan.objects.filter(is_private=False) 
        return render(req, 'index.html', {"flanes_publicos": flanes_publicos})
    

def acerca(req):
    context = {
       "data": "" 
    }
    return render(req, 'about.html', context)

def bienvenido(req):
    context = {
    "message2": "Bienvenid@s a nuestro sitio especialista en Flanes Gourmet",   
    }
    return render(req, 'welcome.html', context)