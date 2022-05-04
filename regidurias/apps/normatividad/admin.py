from django.contrib import admin
from apps.normatividad.models import *

# Register your models here.
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
class NormatividadAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre',)


admin.site.register(Tipo,TipoAdmin)
admin.site.register(Normatividad,NormatividadAdmin)

# Register your models here.
