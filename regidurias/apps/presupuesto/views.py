from django.shortcuts import render
from apps.presupuesto.models import Presupuesto
import locale
from django.views import View
from apps.presupuesto.filters import PresupuestoFilter

# Create your views here.
class PresupuestoView(View):
    def get(self, request, *args, **kwargs):
        presupuesto = Presupuesto.objects.all()
        presupuesto_filter = PresupuestoFilter(request.GET, queryset=presupuesto)
        return render(request, 'presupuesto/template.html', {'filter': presupuesto_filter})