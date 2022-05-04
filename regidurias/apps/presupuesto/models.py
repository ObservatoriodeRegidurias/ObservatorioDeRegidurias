from django.db import models
from apps.entidades.models import Entidades,Municipio

# Create your models here.
class Presupuesto(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='Año')
    presupuesto = models.FloatField( verbose_name='Presupuesto')
    presupuesto_per_capital = models.FloatField(verbose_name='Presupuesto per cápita')
    servicos_personales = models.FloatField( verbose_name='Servicios personales')
    comunicacion_social = models.FloatField( verbose_name='Comunicación social')
    gasto_social = models.FloatField( verbose_name='Gasto social')
    fuentes = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/', verbose_name='fuentes')
    fuentes_dos = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/', verbose_name='fuentes2')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)