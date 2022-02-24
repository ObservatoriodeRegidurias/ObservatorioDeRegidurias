from django.db import models


class Entidades(models.Model):
    entidades = models.CharField(max_length=100,verbose_name='Entidades',default="Some String")

    def __str__(self):
        return self.entidades


class Municipio(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.CharField(max_length=100,verbose_name='Municipio',default="Some String")

    def __str__(self):
        return self.municipio