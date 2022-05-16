from django.contrib import admin
from apps.home.models import *
from embed_video.admin import AdminVideoMixin

class ObservatorioAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
# Register your models here.
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

class AcercaDeNosotrosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Observatorio, ObservatorioAdmin)
admin.site.register(AcercaDeNosotros, AcercaDeNosotrosAdmin)
