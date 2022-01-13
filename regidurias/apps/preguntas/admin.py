from django.contrib import admin
from apps.preguntas.models import *

# Register your models here.
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nombre','email',)

admin.site.register(Comentarios,ComentariosAdmin)

# Register your models here.
