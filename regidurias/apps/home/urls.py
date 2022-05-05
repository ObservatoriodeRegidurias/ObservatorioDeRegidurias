from django.urls import path
from .views import HomeView, NoticiasView

urlpatterns = [

    path('',HomeView.as_view(), name='inicio'),
    #path('<slug:noticias>/',NoticiasView.as_view(), name='noticias'),
]