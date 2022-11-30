from django.urls import path
from .views import menu, leftside, noside, rightside,post

urlpatterns = [
    path('',menu, name='menu'),
    path('blog/',leftside, name='blog'),
    path('reclamo/',noside, name='reclamo'),
    path('recomendacion/',rightside, name='recomendacion'),
    path('articulos/',post, name='post'),
]
