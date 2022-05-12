import re
from django.db import models
import datetime
from datetime import timedelta
from apps.entidades.models import Entidades,Municipio

# Create your models here.
TIPO_DE_SESION_CHOISES=(('1',('Solemne')),
                        ('2',('Ordinaria')),
                        ('3',('Extraordinaria')))

MODALIDAD_CHOISES=(('1',('Presencial')),
                   ('2',('Virtual')))


class SesionesCabildo(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    ayuntamiento = models.CharField(max_length=12, verbose_name='Ayuntamiento')
    fecha = models.DateTimeField(blank=True, null=True, verbose_name='Fecha')
    tipo_de_sesion = models.CharField(max_length=1, choices=TIPO_DE_SESION_CHOISES, verbose_name='Tipo de sesión')
    modalidad = models.CharField(max_length=1,choices=MODALIDAD_CHOISES , verbose_name='Modalidad')
    actas = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/',verbose_name='actas')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)