from django.urls import path
from .views import NormatividadView

urlpatterns = [

    path('',NormatividadView.as_view(), name='normatividad')
]