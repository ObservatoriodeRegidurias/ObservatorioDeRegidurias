from django.db import models
from apps.entidades.models import Entidades,Municipio
# Create your models here.
class Tipo(models.Model):
    tipo = models.CharField(max_length=100,verbose_name='tipo',default="Some String")

    def __str__(self):
        return self.tipo
class Normatividad(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    fuentes = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/', verbose_name='fuentes')
    fecha_de_publicacion = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de publicación')
    ultima_reforma = models.DateTimeField(blank=True, null=True, verbose_name='Ultima reforma')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
