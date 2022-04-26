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


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Noticias.objects.get(slug=slug)
        except Noticias.DoesNotExist:
            raise Http404
        except Noticias.MultipleObjectsReturned:
            article_obj = Noticias.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "home/noticias.html", context=context)