from django.db import models

# Create your models here.
class Presupuesto(models.Model):
    year = models.IntegerField(max_length=4, verbose_name='Año')
    presupuesto = models.FloatField( verbose_name='Presupuesto')
    presupuesto_per_capital = models.FloatField(verbose_name='Presupuesto pre capital')
    servicos_personales = models.FloatField( verbose_name='Servicios personales')
    comunicacion_social = models.FloatField( verbose_name='Comunicación social')
    gasto_social = models.FloatField( verbose_name='Gasto social')
    fuentes = models.ImageField(upload_to='pdf', blank=True, verbose_name='fuentes')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)