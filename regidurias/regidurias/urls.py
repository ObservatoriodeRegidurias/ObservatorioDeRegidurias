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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesion_cabildo/',include(('apps.cabildo.urls','sesion_cabildo'))),
    path('contacto/',include(('apps.cabildo.urls','contacto'))),
    path('home/',include(('apps.cabildo.urls','home'))),
    path('normatividad/',include(('apps.cabildo.urls','normatividad'))),
    path('preguntas/',include(('apps.cabildo.urls','reguntas'))),
    path('presupuesto/',include(('apps.cabildo.urls','presupuesto'))),
    path('regidurias/',include(('apps.cabildo.urls','regidurias')))
]
