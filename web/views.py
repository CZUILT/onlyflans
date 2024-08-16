from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(req):
    context = {
        "message": "Bienvenid@s a OnlyFlans",
        "urls": ["https://st.depositphotos.com/1290614/3840/i/450/depositphotos_38408239-stock-photo-assorted-desserts.jpg","https://www.recetasnestlecam.com/sites/default/files/2023-02/postres-con-mango.jpg.jpg"],
        "user": {"username": "Pepe", "password": 1234, "is_active": False},
        "productos": [{"name": "TV", "url":"vvv"},{"name": "celu", "url":"vvv"},{"name": "tablet", "url":"vvv"} ]
    }
    return render(req, 'index.html', context)

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