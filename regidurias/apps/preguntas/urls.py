from django.urls import path
from .views import PreguntasView

urlpatterns = [

    path('<int:pk>',PreguntasView.as_view(), name='preguntas')
]