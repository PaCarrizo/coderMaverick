from django.urls import path
from .views import menu, pagblog, pagreclamos, pagrecomendaciones,post

urlpatterns = [
    path('',menu, name='menu'),
    path('blog/',pagblog, name='blog'),
    path('reclamo/',pagreclamos, name='reclamo'),
    path('recomendacion/',pagrecomendaciones, name='recomendacion'),
    path('articulos/',post, name='post'),
]
