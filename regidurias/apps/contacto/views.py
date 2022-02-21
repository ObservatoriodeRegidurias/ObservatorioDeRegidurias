from django.shortcuts import render
from apps.contacto.models import Contacto
import locale
from django.views import View

# Create your views here.
class ContactoView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contacto/template.html', locals())