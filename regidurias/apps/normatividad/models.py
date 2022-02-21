from django.db import models

# Create your models here.
TIPO_DE_NORMA_CHOISES=(('1',('Ley general')),
                    ('2',('Reglamento municipal')),
                    ('3',('Ley local')),
                    ('4',('Reglamento municipal')))


class Normatividad(models.Model):
    tipo_de_let = models.CharField(max_length=1, choices=TIPO_DE_NORMA_CHOISES, verbose_name='Tipo de sesión')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    fuentes = models.ImageField(upload_to='pdf', blank=True, verbose_name='fuentes')
    fecha_de_publicacion = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de publicación')
    ultima_reforma = models.DateTimeField(blank=True, null=True, verbose_name='Ultima reforma')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
