from django.shortcuts import render
from apps.normatividad.models import Normatividad
import locale
from django.views import View

# Create your views here.
class NormatividadView(View):
    def get(self, request, *args, **kwargs):
        normatividad = Normatividad.objects.all().order_by('-created_at')
        return render(request, 'normatividad/template.html', locals())