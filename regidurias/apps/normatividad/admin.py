from django.contrib import admin
from apps.normatividad.models import *

# Register your models here.
class SesionesCabildoAdmin(admin.ModelAdmin):
    list_display = ('entidad','tipo_de_let', 'nombre',)

admin.site.register(SesionesCabildo,SesionesCabildoAdmin)

# Register your models here.
