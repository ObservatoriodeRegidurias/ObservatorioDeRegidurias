from django.shortcuts import render
from apps.home.models import Event,Noticias,Observatorio
import locale
from django.views import View
from django.http import Http404
from django.shortcuts import render, redirect
# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        event =  Event.objects.filter(status=2).order_by('-created_at')
        noticia = Noticias.objects.filter(status=2).order_by('-created_at')
        observatorio = Observatorio.objects.all().order_by('-created_at')
        return render(request, 'home/template.html', locals())



class NoticiasView(View):
    @property
    def noticia(self):
        return self.kwargs.get('noticias')

    def get(self, request, *args, **kwargs):
        noticia = Noticias.objects.filter(slug=self.noticia) 
        print('noticias', noticia)  
        return render(request, 'home/template.html', locals())