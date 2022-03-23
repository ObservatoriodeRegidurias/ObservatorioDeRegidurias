from django.db import models
from apps.entidades.models import Entidades,Municipio
# Create your models here.

class Comision_1_presidencia(models.Model):
    comision_1_presidencia = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.comision_1_presidencia

class Comision_2_presidencia(models.Model):
    comision_2_presidencia = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.comision_2_presidencia

class Comision_1_secretaria(models.Model):
    Comision_1_secretaria = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_1_secretaria

class Comision_2_secretaria(models.Model):
    Comision_2_secretaria = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_2_secretaria

class Comision_3_secretaria(models.Model):
    Comision_3_secretaria = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_3_secretaria

class Comision_4_secretaria(models.Model):
    Comision_4_secretaria = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_4_secretaria


class Comision_1(models.Model):
    Comision_1 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_1

class Comision_2(models.Model):
    Comision_2 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_2

class Comision_3(models.Model):
    Comision_3 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_3

class Comision_4(models.Model):
    Comision_4 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_4

class Comision_5(models.Model):
    Comision_5 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.comision_5

class Comision_6(models.Model):
    Comision_6 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_6


class Comision_7(models.Model):
    Comision_7 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_7

class Comision_8(models.Model):
    Comision_8 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_8

class Comision_9(models.Model):
    Comision_9 = models.CharField(max_length=100,verbose_name='comision',default="Some String")

    def __str__(self):
        return self.Comision_9

class Partido(models.Model):
    partido = models.CharField(max_length=100,verbose_name='partido',default="Some String")

    def __str__(self):
        return self.partido

CARGO_CHOISES=(('1',('Presidente Muncipal')),
                ('2',('Suplente Presidente')),
                ('3',('Síndico Procurador')),
                ('4',('Suplente Síndico')),
                ('5',('Regidor MR')),
                ('6',('Regidor RP')))

GENERO_CHOISES=(('1',('Femenino')),
                ('2',('Masculino')),
                ('3',('No binario')))


STATUS_CHOICES = (('1',('Borrador')),
                ('2',('Publicado')),
                ('3',('Finalizado')))


class Regidurias(models.Model):
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    ayuntamiento = models.CharField(max_length=12, verbose_name='Ayuntamiento')
    cargo = models.CharField(max_length=2, choices=CARGO_CHOISES, verbose_name='Cargo')
    genero = models.CharField(max_length=1,default=1, choices=GENERO_CHOISES, verbose_name='Genero')
    nombre = models.CharField(max_length=300, verbose_name='nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido materno')
    nombre_suplente = models.CharField(max_length=300, default="Some String",  verbose_name='Nombre del suplente')
    apellido_paterno_suplente = models.CharField(max_length=100, default="Some String", verbose_name='Apellido paterno del suplente')
    apellido_materno_suplente = models.CharField(max_length=120, default="Some String", verbose_name='Apellido materno del suplente')
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='img', blank=True, verbose_name='Foto')
    telefono = models.IntegerField(max_length=10, verbose_name='Telefono')
    correo = models.CharField(max_length=120, verbose_name='Correo')
    facebook = models.URLField(blank=True, null=True, name="facebook", verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, name="twitter", verbose_name="Twitter")
    instagram = models.URLField(blank=True, null=True, name="instagram", verbose_name="Instagram")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default=1,)
    comision_1_presidencia = models.ForeignKey(Comision_1_presidencia, on_delete=models.CASCADE)
    comision_2_presidencia = models.ForeignKey(Comision_2_presidencia, on_delete=models.CASCADE)
    comision_1_secretaria = models.ForeignKey(Comision_1_secretaria, on_delete=models.CASCADE)
    comision_2_secretaria = models.ForeignKey(Comision_2_secretaria, on_delete=models.CASCADE)
    comision_3_secretaria = models.ForeignKey(Comision_3_secretaria, on_delete=models.CASCADE)
    comision_4_secretaria = models.ForeignKey(Comision_4_secretaria, on_delete=models.CASCADE)
    comision_1 = models.ForeignKey(Comision_1, on_delete=models.CASCADE)
    comision_2 = models.ForeignKey(Comision_2, on_delete=models.CASCADE)
    comision_3 = models.ForeignKey(Comision_3, on_delete=models.CASCADE)
    comision_4 = models.ForeignKey(Comision_4, on_delete=models.CASCADE)
    comision_5 = models.ForeignKey(Comision_5, on_delete=models.CASCADE)
    comision_6 = models.ForeignKey(Comision_6, on_delete=models.CASCADE)
    comision_7 = models.ForeignKey(Comision_7, on_delete=models.CASCADE)
    comision_8 = models.ForeignKey(Comision_8, on_delete=models.CASCADE)
    comision_9 = models.ForeignKey(Comision_9, on_delete=models.CASCADE)
    actas = models.FileField(blank=True, null=True, upload_to='chapters/%Y/%m/%D/',verbose_name='actas')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
