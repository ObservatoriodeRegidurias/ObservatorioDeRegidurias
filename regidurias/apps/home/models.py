from django.db import models
from embed_video.fields import EmbedVideoField
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
#from .utils import slugify_instance_title
STATUS_CHOICES = (('1',('Borrador')),
                ('2',('Publicado')),
                ('3',('Finalizado')))
# Create your models here.
class   Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(verbose_name="descripcion",default="Some String")
    nota = models.TextField(max_length=3000,blank=True, null=True, name="nota", verbose_name="noticia",default="Some String")
    imagen = models.ImageField (upload_to='noticias', blank=True, null=True)
    link = models.CharField(max_length=320,blank=True, null=True, name="link", verbose_name="noticias_link")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)
    slug = models.CharField(unique=True,max_length=1000, null=True, blank=True, default="borrar este campo")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     @property
#     def name(self):
#         return self.titulo

#     def get_absolute_url(self):
#         return reverse("noticias:detail", kwargs={"slug": self.slug})

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)


# def noticias_pre_save(sender, instance, *args, **kwargs):
#     if instance.slug is None:
#         slugify_instance_title(instance, save=False)

# pre_save.connect(noticias_pre_save, sender=Noticias)


# def noticias_post_save(sender, instance, created, *args, **kwargs):
# # print('post_save')
#     if created:
#         slugify_instance_title(instance, save=True)

# post_save.connect(noticias_post_save, sender=Noticias)
class Event(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField (upload_to='carrucel', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default=1,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Observatorio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    link_cabildo = EmbedVideoField(default="Some String")
    path_thumbnail = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class AcercaDeNosotros(models.Model):
    imagen = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen1 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen2 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen3 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen4 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen5 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen6 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen7 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen8 = models.ImageField (upload_to='logos', blank=True, null=True)
    imagen9 = models.ImageField (upload_to='logos', blank=True, null=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(verbose_name="Acerca de nosotros")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    