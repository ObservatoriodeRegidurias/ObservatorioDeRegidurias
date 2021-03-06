from django.db import models
from django.utils import timezone
# Create your models here.

class Comentarios(models.Model):
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    asunto = models.CharField(max_length=200)
    comentario = models.TextField()
    resolve = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class ComentariosPost(models.Model):
    resolve = models.TextField()
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now)