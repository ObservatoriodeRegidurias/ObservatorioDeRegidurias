from django.shortcuts import render
from apps.contacto.models import Contacto
import locale
from django.views import View
from apps.contacto.form import ContactoForm
from django.contrib import messages
# Create your views here.
class ContactoView(View):
    @property
    def id(self):
        return self.kwargs.get('create_email')

    def get(self, request, *args, **kwargs):
        if self.id:
            contact = Contacto.objects.get(id=self.id)
            form = ContactoForm(instance=contact)
        else:
            form = ContactoForm()
        return render(request, 'contacto/template.html', locals())

    def post(self, request, *args, **kwargs):
        if self.id:
            contact = Contacto.objects.get(id=self.id)
            form = ContactoForm(request.POST, request.FILES, instance=contact)
        else:
            form = ContactoForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, ("Tú email se mando con exito"))
            return render(request, 'contacto/template.html', locals())
        else:   
            messages.error(request,('No se mando el email'))
            return render(request, 'contacto/template.html', locals())