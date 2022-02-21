from django.urls import path
from .views import PresupuestoView

urlpatterns = [

    path('',PresupuestoView.as_view(), name='presupuesto')
]