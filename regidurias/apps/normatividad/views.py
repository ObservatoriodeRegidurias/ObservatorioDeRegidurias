from django.shortcuts import render
from apps.normatividad.models import Normatividad
import locale
from django.views import View
from apps.normatividad.filters import NormatividadFilter

# Create your views here.
class NormatividadView(View):
    def get(self, request, *args, **kwargs):
        normatividad = Normatividad.objects.all()
        normatividad_filter = NormatividadFilter(request.GET, queryset=normatividad)
        return render(request, 'normatividad/template.html', {'filter': normatividad_filter})