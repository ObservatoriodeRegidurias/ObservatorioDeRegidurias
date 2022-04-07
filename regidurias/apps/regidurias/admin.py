from django.contrib import admin
from apps.regidurias.models import *

# Register your models here.
class Comision_1_presidenciaAdmin(admin.ModelAdmin):
    list_display = ('comision_1_presidencia',)

class Comision_2_presidenciaAdmin(admin.ModelAdmin):
    list_display = ('comision_2_presidencia',)

class Comision_uno_secretariaAdmin(admin.ModelAdmin):
    list_display = ('Comision_1_secretaria',)

class Comision_2_secretariaAdmin(admin.ModelAdmin):
    list_display = ('Comision_2_secretaria',)

class Comision_3_secretariaAdmin(admin.ModelAdmin):
    list_display = ('Comision_3_secretaria',)

class Comision_4_secretariaAdmin(admin.ModelAdmin):
    list_display = ('Comision_4_secretaria',)

class Comision_1Admin(admin.ModelAdmin):
    list_display = ('Comision_1',)

class Comision_2Admin(admin.ModelAdmin):
    list_display = ('Comision_2',)

class Comision_3Admin(admin.ModelAdmin):
    list_display = ('Comision_3',)

class Comision_4Admin(admin.ModelAdmin):
    list_display = ('Comision_4',)

class Comision_5Admin(admin.ModelAdmin):
    list_display = ('Comision_5',)

class Comision_6Admin(admin.ModelAdmin):
    list_display = ('Comision_6',)

class Comision_7Admin(admin.ModelAdmin):
    list_display = ('Comision_7',)

class Comision_8Admin(admin.ModelAdmin):
    list_display = ('Comision_8',)

class Comision_9Admin(admin.ModelAdmin):
    list_display = ('Comision_9',)

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('partido',)

class RegidoresAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Comision_1_presidencia, Comision_1_presidenciaAdmin)
admin.site.register(Comision_2_presidencia, Comision_2_presidenciaAdmin)
admin.site.register(Comision_1_secretaria, Comision_uno_secretariaAdmin)
admin.site.register(Comision_2_secretaria, Comision_2_secretariaAdmin)
admin.site.register(Comision_3_secretaria, Comision_3_secretariaAdmin)
admin.site.register(Comision_4_secretaria, Comision_4_secretariaAdmin)
admin.site.register(Comision_1, Comision_1Admin)
admin.site.register(Comision_2, Comision_2Admin)
admin.site.register(Comision_3, Comision_3Admin)
admin.site.register(Comision_4, Comision_4Admin)
admin.site.register(Comision_5, Comision_5Admin)
admin.site.register(Comision_6, Comision_6Admin)
admin.site.register(Comision_7, Comision_7Admin)
admin.site.register(Comision_8, Comision_8Admin)
admin.site.register(Comision_9, Comision_9Admin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Regidurias, RegidoresAdmin)
