from django.urls import path
from .views import CabildoView

urlpatterns = [

    path('',CabildoView.as_view(), name='cabildo')
]