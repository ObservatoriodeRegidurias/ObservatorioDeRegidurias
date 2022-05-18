from django.urls import path
from .views import HomeView, NoticiasView,AcercaDeNosotrosView

urlpatterns = [

    path('',HomeView.as_view(), name='inicio'),
    path('nosotros/',AcercaDeNosotrosView.as_view(), name='nosotros'),
    #path('<slug:noticias>/',NoticiasView.as_view(), name='noticias'),
]