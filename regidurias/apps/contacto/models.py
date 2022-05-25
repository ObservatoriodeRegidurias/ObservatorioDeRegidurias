from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    asunto = models.CharField(max_length=200)
    mensaje = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.nombre