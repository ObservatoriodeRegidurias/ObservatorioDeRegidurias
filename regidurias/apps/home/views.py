from django.shortcuts import render
from apps.home.models import Event,Noticias,Observatorio
import locale
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        event =  Event.objects.filter(status=2).order_by('-created_at')
        noticia = Noticias.objects.filter(status=2).order_by('-created_at')
        observatorio = Observatorio.objects.all().order_by('-created_at')
        return render(request, 'home/template.html', locals())
