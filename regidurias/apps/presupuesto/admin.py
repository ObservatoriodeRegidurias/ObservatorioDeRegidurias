from django.contrib import admin
from apps.presupuesto.models import *

# Register your models here.
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('year', 'presupuesto')

admin.site.register(Presupuesto,PresupuestoAdmin)
