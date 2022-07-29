from django.urls import path
from .views import ComentariosView, PostView, PostCreateView

urlpatterns = [

    path('', ComentariosView.as_view(), name='preguntas'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    # path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]