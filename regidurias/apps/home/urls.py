from django.urls import path
from .views import HomeView
from .views import (
    article_detail_view
)
urlpatterns = [

    path('',HomeView.as_view(), name='inicio'),
    path('<slug:slug>/',article_detail_view, name='noticias')
]