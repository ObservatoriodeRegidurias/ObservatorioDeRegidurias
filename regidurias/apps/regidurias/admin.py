from django.contrib import admin
from apps.regidurias.models import *

# Register your models here.
class RegidoresAdmin(admin.ModelAdmin):
    list_display = ('nombre','year','comision_1')

admin.site.register(Regidores, RegidoresAdmin)
