from django.shortcuts import render
from apps.regidurias.models import Regidores
import locale
from django.views import View

# Create your views here.
class RegiduriasView(View):
    def get(self, request, *args, **kwargs):
        regidores =  Regidores.objects.all().order_by('-created_at')
        return render(request, 'regidurias/template.html', locals())
