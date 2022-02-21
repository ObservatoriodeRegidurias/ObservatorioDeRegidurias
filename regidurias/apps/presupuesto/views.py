from django.shortcuts import render
from apps.presupuesto.models import Presupuesto
import locale
from django.views import View

# Create your views here.
class PresupuestoView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'presupuesto/template.html', locals())