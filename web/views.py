from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    flanes_publicos = Flan.objects.filter(is_private=False) # Carga los flanes dependiendo si "private=False"
    return render(req, 'index.html', {"flanes_publicos": flanes_publicos})

@login_required # permite acceder al path o link solo si se está auth
def welcome(req):
    private_flans = Flan.objects.filter(is_private=True)
    return render(req, 'welcome.html', {"private_flans": private_flans})

def about(req):
    return render(req, 'about.html', {})

def nueva_vista(req):
    context = {
        "username": "César"
    }
    return render(req, 'nueva_vista.html', context)

def contacto(req):
    if req.method == 'POST':

        #*FORM
        form = ContactFormForm(req.POST)
        if form.is_valid():
            #*MODEL
            ContactForm.objects.create(**form.cleaned_data)# Pasamos la data del diccionario .cleanned_data a argumentos
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
    return render(req, 'contactus.html', {'form': form})

def exito(req):
    return render(req, 'success.html', {})