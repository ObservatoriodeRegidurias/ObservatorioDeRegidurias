"""regidurias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles import staticfiles_urlpattern
from apps.regidurias.views import RegiduriasView, RegidorView
from apps.cabildo.views import CabildoView
from apps.contacto.views import ContactoView
from apps.normatividad.views import NormatividadView
from apps.preguntas.views import PreguntasView
from apps.presupuesto.views import PresupuestoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesion_cabildo/',include(('apps.cabildo.urls','sesion_cabildo'))),
    path('contacto/',include(('apps.contacto.urls','contacto'))),
    path('',include(('apps.home.urls','home'))),
    path('normatividad/',include(('apps.normatividad.urls','normatividad'))),
    path('preguntas/',include(('apps.preguntas.urls','preguntas'))),
    path('presupuesto/',include(('apps.presupuesto.urls','presupuesto'))),
    path('regidurias/',include(('apps.regidurias.urls','regidurias'))),
    path('regidurias/',RegiduriasView.as_view(), name='regidurias'),
    path('sesion_cabildo/',CabildoView.as_view(), name='sesion_cabildo'),
    path('contacto/',ContactoView.as_view(), name='contacto'),
    path('normatividad/',NormatividadView.as_view(), name='normatividad'),
    path('preguntas/',PreguntasView.as_view(), name='preguntas'),
    path('presupuesto/',PresupuestoView.as_view(), name='presupuesto'),
    path('regidor/',RegidorView.as_view(), name='regidor')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns+=staticfiles_urlpattern()