from django.urls import path
from .views import RegiduriasView, RegidorView

urlpatterns = [

    path('regidurias/',RegiduriasView.as_view(), name='regidurias'),
    path('regidor/',RegidorView.as_view(), name='regidor')
]