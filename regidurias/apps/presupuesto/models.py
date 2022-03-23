from django.db import models
from apps.entidades.models import Entidades,Municipio

# Create your models here.
class Presupuesto(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    year = models.IntegerField(max_length=4, verbose_name='Año')
    presupuesto = models.FloatField( verbose_name='Presupuesto')
    presupuesto_per_capital = models.FloatField(verbose_name='Presupuesto per capital')
    servicos_personales = models.FloatField( verbose_name='Servicios personales')
    comunicacion_social = models.FloatField( verbose_name='Comunicación social')
    gasto_social = models.FloatField( verbose_name='Gasto social')
    fuentes = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/', verbose_name='fuentes')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)