from django.db import models

# Create your models here.

CARGO_CHOISES=(('1',('Presidente Muncipal')),
                ('2',('Suplente Presidente')),
                ('3',('Síndico Procurador')),
                ('4',('Suplente Síndico')),
                ('5',('Regidor MR')),
                ('6',('Regidor RP')),
                ('7',('Suplente Regidor')),
                ('8',('Presidenta Muncipal')),
                ('9',('Suplente Presidenta')),
                ('10',('Síndica Procurador')),
                ('11',('Suplente Síndica')),
                ('12',('Regidora MR')),
                ('13',('Regidora RP')),
                ('14',('Suplente Regidora')))

PARTIDO_CHOISES=(('1',('Morena')),
                ('2',('Partido Verde Ecologísta')),
                ('3',('Partido del Trabajo')),
                ('4',('Partido de la Revolución Democrática')),
                ('5',('Partido Accion Nacional')),
                ('6',('Partido Revolucionario Institucional')),
                ('7',('Movimiento Ciudadano')),
                ('8',('Sin Partido')))

COMISIONES_CHOISES=(('1',('Gobernación, Legislación y Mejora Regulatoria')),
                ('2',('Hacienda y Patrimonio Municipal')),
                ('3',('Transparencia, Rendición de Cuentas y Combate a la Corrupción')),
                ('4',('Seguridad Ciudadana y Protección Civil')),
                ('5',('Planeación, Urbanismo, Obras y Servicios Públicos')),
                ('6',('Medio Ambiente, Desarrollo Sustentable y Salud')),
                ('7',('Vialidad y Movilidad Urbana')),
                ('8',('Desarrollo Metropolitano')),
                ('9',('Educación, Cultura, Bibliotecas, Ciencia y Tecnología')),
                ('10',('Juventud y Deporte')),
                ('11',('Bienestar Social')),
                ('12',('Desarrollo Económico, Turismo y Asuntos Fronterizos')),
                ('13',('Recreación, Espectáculos y Alcoholes')),
                ('14',('Igualdad de Género')),
                ('15',('Derechos Humanos, Migración y Asuntos Indígenas')),
                ('16',('Participación Ciudadana')),
                ('17',('Régimen Interno')),
                ('18',('Planeación, Urbanismo, Desarrollo Metropolitano, Obras y Servicios Públicos')),
                ('19',('Coordinación Política')))


class Regidores(models.Model):
    entidad = models.CharField(max_length=200, verbose_name='Entidad')
    municipio = models.CharField(max_length=200, verbose_name='Municipio')
    year = models.CharField(max_length=9, verbose_name='Año')
    ayuntamiento = models.CharField(max_length=12, verbose_name='Ayuntamiento')
    cargo = models.CharField(max_length=2, choices=CARGO_CHOISES, verbose_name='Cargo')
    cargo_secundario = models.CharField(max_length=1, choices=CARGO_CHOISES, verbose_name='Cargo secundario')
    nombre = models.CharField(max_length=300, verbose_name='nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido materno')
    partido = models.CharField(max_length=1, choices=PARTIDO_CHOISES, verbose_name='Partido')
    foto = models.ImageField(upload_to='img', blank=True, verbose_name='Foto')
    telefono = models.IntegerField(max_length=10, verbose_name='Telefono')
    correo = models.CharField(max_length=120, verbose_name='Correo')
    facebook = models.URLField(blank=True, null=True, name="facebook", verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, name="twitter", verbose_name="Twitter")
    instagram = models.URLField(blank=True, null=True, name="instagram", verbose_name="Instagram")
    comision_1 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 1')
    comision_2 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 2')
    comision_3 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 3')
    comision_4 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 4')
    comision_5 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 5')
    comision_6 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 6')
    comision_7 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 7')
    comision_8 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 8')
    comision_9 = models.CharField(max_length=2, choices=COMISIONES_CHOISES, verbose_name='Comisión 9')
    inicio_de_funciones = models.DateTimeField(blank=True, null=True, verbose_name='Inicio de funciones')
    termina_funciones = models.DateTimeField(blank=True, null=True, verbose_name='Termina funciones')
    actas = models.ImageField(upload_to='pdf', blank=True, verbose_name='actas')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
