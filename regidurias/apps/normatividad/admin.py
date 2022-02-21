from django.contrib import admin
from apps.normatividad.models import *

# Register your models here.
class NormatividadAdmin(admin.ModelAdmin):
    list_display = ('tipo_de_let', 'nombre',)

admin.site.register(Normatividad,NormatividadAdmin)

# Register your models here.
