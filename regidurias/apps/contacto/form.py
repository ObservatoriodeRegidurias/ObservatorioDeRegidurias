from django import forms
from apps.contacto.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'app-form-control', 'placeholder': 'Nombre'}),
            'email': forms.TextInput(attrs={'class': 'app-form-control', 'placeholder': 'Email'}),
            'asunto': forms.TextInput(attrs={'class': 'app-form-control', 'placeholder': 'Asunto'}),
            'mensaje':  forms.TextInput(attrs={'class': 'app-form-control' , 'placeholder': 'Mensaje'}),
        }