from django.shortcuts import render
from apps.home.models import Event,Noticias,Observatorio, AcercaDeNosotros
import locale
from django.views import View
from django.http import Http404
from django.shortcuts import render, redirect
# Create your views here.
class HomeView(View):
    @property
    def noticias(self):
        return self.kwargs["noticias"]

    def get(self, request, *args, **kwargs):
        event =  Event.objects.filter(status=2).order_by('-created_at')
        noticia = Noticias.objects.filter(status=2).order_by('-created_at')
        observatorio = Observatorio.objects.all().order_by('-created_at')
        return render(request, 'home/template.html', locals())



class NoticiasView(View):
    def get(self, request, *args, **kwargs):
        noticia = Noticias.objects.all().order_by('-created_at')
        return render(request, 'home/noticias.html', locals())

class AcercaDeNosotrosView(View):
    def get(self, request, *args, **kwargs):
        nosotros = AcercaDeNosotros.objects.all()
        return render(request, 'home/quien.html', locals())