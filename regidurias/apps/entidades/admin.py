from django.contrib import admin
from apps.entidades.models import *

# Register your models here.
class EntidadesAdmin(admin.ModelAdmin):
    list_display = ('entidades',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio',)


admin.site.register(Entidades, EntidadesAdmin)
admin.site.register(Municipio, MunicipioAdmin)