from django.urls import path
from .views import RegiduriasView

urlpatterns = [

    path('regidurias/',RegiduriasView.as_view(), name='regidurias')
]