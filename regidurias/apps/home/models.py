from django.db import models

STATUS_CHOICES = (('1',('Borrador')),
                ('2',('Publicado')),
                ('3',('Finalizado')))
# Create your models here.
class   Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField (upload_to='noticias', blank=True, null=True)
    link = models.URLField(blank=True, null=True, name="noticias_link", verbose_name="noticias_link")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Event(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField (upload_to='carrucel', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default=1,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Observatorio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    link_cabildo = models.URLField(blank=True, null=True, name="cabildo_link", verbose_name="cabildo_link")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)