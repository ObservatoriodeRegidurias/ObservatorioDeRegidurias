from django.shortcuts import render,redirect,reverse
from apps.regidurias.models import Regidurias
import locale
from django.views import View
from apps.regidurias.filters import RegiduriasFilter 
from django.views import generic
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

class regidor_detail(generic.ListView):
    model = Regidurias
    template_name = "regidurias/regidor.html"
    # @property
    # def regidurias(self):
    #     return self.kwargs.get('regidurias')
        
    # def get(self, request, *args, **kwargs):
    #     regidurias = Regidurias.objects.get(slug=self.regidurias)
    #     #regidurias =  Regidurias.objects.filter(slug=self.regidurias).first()
    #     return render(request, "regidurias/regidor.html", locals())