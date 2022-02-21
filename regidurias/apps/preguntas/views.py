from django.shortcuts import render
from apps.preguntas.models import Comentarios
import locale
from django.views import View

# Create your views here.
class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        Preguntas =  Comentarios.objects.all().order_by('-created_at')
        return render(request, 'preguntas/template.html', locals())