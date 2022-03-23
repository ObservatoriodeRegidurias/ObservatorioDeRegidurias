from django.shortcuts import render
from apps.regidurias.models import Regidurias
import locale
from django.views import View

# Create your views here.
class RegiduriasView(View):
    def get(self, request, *args, **kwargs):
        regidores =  Regidurias.objects.all().order_by('-created_at')
        return render(request, 'regidurias/template.html', locals())
