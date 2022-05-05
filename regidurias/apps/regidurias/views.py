from django.shortcuts import render,redirect,reverse
from apps.regidurias.models import Regidurias
import locale
from django.views import View
from apps.regidurias.filters import RegiduriasFilter 

# Create your views here.
class RegiduriasView(View):
    @property
    def regidurias(self):
        return self.kwargs["regidurias"]

    def get(self, request, *args, **kwargs):
        regidores =  Regidurias.objects.filter(status=2)
        regidores_filter = RegiduriasFilter(request.GET, queryset=regidores)
        #return render(reverse("regidurias/template.html", kwargs={"regidurias": regidores.slug}))
        return render(request, 'regidurias/template.html', {'filter': regidores_filter})

class RegidorView(View):
    @property
    def regidurias(self):
        return self.kwargs["regidurias"]
        
    def get(self, request, *args, **kwargs):
        regidor =  Regidurias.objects.filter(slug=self.regidurias).first()
        return render(reverse("regidurias/template.html", kwargs={"regidurias": regidor.slug}))
