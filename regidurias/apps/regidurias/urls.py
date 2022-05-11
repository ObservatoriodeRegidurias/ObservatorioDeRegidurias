from django.urls import path
from .views import RegiduriasView,RegidorDetailView#, RegidorView

app_name = 'regidor'

urlpatterns = [
   
    path('regidurias/',RegiduriasView.as_view(), name='regidurias'),
    #path('regidor/<str:slug>/',RegidorView.as_view(), name='regidor')
    path('regidor/<str:slug>/',RegidorDetailView.as_view(), name='regidor')

]