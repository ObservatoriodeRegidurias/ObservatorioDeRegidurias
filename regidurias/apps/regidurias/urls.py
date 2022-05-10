from django.urls import path
from .views import RegiduriasView
#from .views import views
urlpatterns = [
   
    path('regidurias/',RegiduriasView.as_view(), name='regidurias'),
    #path('regidor/<str:slug>/',views.regidor_detail.as_view(), name='regidor')
]