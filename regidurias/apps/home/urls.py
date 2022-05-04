from django.urls import path
from .views import HomeView
# from .views import (
#     article_detail_view
# )
urlpatterns = [

    path('',HomeView.as_view(), name='inicio'),
    # path('<slug:noticias>/',NoticiasView.as_view(), name='noticias'),
]