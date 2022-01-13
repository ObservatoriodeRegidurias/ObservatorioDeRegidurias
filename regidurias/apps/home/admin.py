from tkinter import E
from django.contrib import admin
from apps.home.models import *

# Register your models here.
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

class ObservatorioAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Observatorio, ObservatorioAdmin)
