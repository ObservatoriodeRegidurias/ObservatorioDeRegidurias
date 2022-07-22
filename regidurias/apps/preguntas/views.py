from django.shortcuts import render
from apps.preguntas.models import Comentarios, ComentariosPost
from apps.preguntas.form import ComentariosForm, ComentariosPostForm
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
import locale
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class PreguntasView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        post = Comentarios.objects.get(pk=pk)
        form = ComentariosForm()

        comments = ComentariosPost.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments':comments
        }

        return render(request, 'preguntas/template.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Comentarios.objects.get(pk=pk)
        form = ComentariosForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()

        comments = ComentariosPost.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments':comments
        }

        return render(request, 'preguntas/template.html', context)
