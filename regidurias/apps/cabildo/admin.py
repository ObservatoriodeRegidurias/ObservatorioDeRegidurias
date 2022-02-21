from re import L
from django.contrib import admin
from apps.cabildo.models import SesionesCabildo

# Register your models here.
class SesionesCabildoAdmin(admin.ModelAdmin):
    list_display = ('ayuntamiento', 'fecha',)

admin.site.register(SesionesCabildo, SesionesCabildoAdmin )
