from django.urls import path
from .views import PreguntasView

urlpatterns = [

    path('',PreguntasView.as_view(), name='preguntas')
]