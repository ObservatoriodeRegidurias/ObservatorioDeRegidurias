from django.shortcuts import render,redirect
from apps.regidurias.models import Regidurias
import locale
from django.views import View
from apps.regidurias.filters import RegiduriasFilter 

# Create your views here.
class RegiduriasView(View):
    def get(self, request, *args, **kwargs):
        regidores =  Regidurias.objects.all()
        regidores_filter = RegiduriasFilter(request.GET, queryset=regidores)
        return render(request, 'regidurias/template.html', {'filter': regidores_filter})
