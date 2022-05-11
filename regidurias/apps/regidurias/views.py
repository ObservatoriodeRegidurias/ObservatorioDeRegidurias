from django.shortcuts import render,redirect,reverse
from apps.regidurias.models import Regidurias
import locale
from django.views import View
from apps.regidurias.filters import RegiduriasFilter 
from django.views import generic
from django.views.generic.detail import DetailView
# Create your views here.
class RegiduriasView(View):
    @property
    def regidurias(self):
        return self.kwargs["regidurias"]

    def get(self, request, *args, **kwargs):
        regidores =  Regidurias.objects.all().exclude(status=1)
        regidores_filter = RegiduriasFilter(request.GET, queryset=regidores)
        #return render(reverse("regidurias/template.html", kwargs={"regidurias": regidores.slug}))
        return render(request, 'regidurias/template.html', {'filter': regidores_filter})


class RegidorDetailView(DetailView):

    model = Regidurias
    template_name = 'regidurias/regidor.html'
    context_object_name = 'regidor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Regidurias.objects.filter(slug=self.kwargs.get('slug'))

        return context
# class RegidorView(View):
#     # @property
#     # def regidurias(self):
#     #     return self.kwargs.get('regidurias')
        
#     def get(self, request, *args, **kwargs):
#         regidurias = Regidurias.objects.get(slug=self.regidurias)
#         #regidurias =  Regidurias.objects.filter(slug=self.regidurias).first()
#         return render(request, "regidurias/regidor.html", locals())