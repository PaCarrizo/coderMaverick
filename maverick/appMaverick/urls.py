from django.urls import path
from .views import menu, leftside, noside, rightside

urlpatterns = [
    path('',menu, name='menu'),
    path('izquierda/',leftside, name='izquierda'),
    path('barra/',noside, name='barra'),
    path('derecha/',rightside, name='derecha'),
]
