from django.contrib import admin
from apps.contacto.models import *

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email',)

admin.site.register(Contacto,ContactoAdmin)
