from django import forms
from django.contrib.auth.models import User
from .models import ContactForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

# Formulario Alternativo:
# para usar se debe modificar en VIEWS.PY ContactFormForm por ContactModelForm
class ContactModelForm(forms.ModelForm):
    
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

