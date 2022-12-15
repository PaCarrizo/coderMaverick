from django.urls import path
from .views import menu, pagblog, pagreclamos, pagrecomendaciones,post,listaRecomendacion,listaReclamos
from .views import BlogDelete,BlogEdit,RecomendacionList,RecomendacionDetalle,RecomendacionEdit,RecomendacionDelete,ReclamosDelete,ReclamosDetalle,ReclamosList,ReclamosEdit

urlpatterns = [
    path('',menu, name='menu'),
    path('blog/',pagblog, name='blog'),
    path('reclamo/',pagreclamos, name='reclamo'),
    path('recomendacion/',pagrecomendaciones, name='recomendacion'),
    path('articulos/',post, name='post'),

    path('editBlog/<pk>/',BlogEdit.as_view(), name='editPost'),
    path('deleteBlog/<pk>/',BlogDelete.as_view(), name='deletePost'),

    #path('listaReco/',RecomendacionList.as_view(), name='listRecomendacion'),
    path('listaReco/',listaRecomendacion, name='listRecomendacion'),
    path('detalleReco/<pk>/',RecomendacionDetalle.as_view(), name='detalleRecomendacion'),
    path('editReco/<pk>/',RecomendacionEdit.as_view(), name='editRecomendacion'),
    path('deleteReco/<pk>/',RecomendacionDelete.as_view(), name='deleteRecomendacion'),

    path('listaReclam/',listaReclamos, name='listReclamos'),
    #path('listaReclam/',ReclamosList.as_view(), name='listReclamos'),
    path('detalleReclam/<pk>/',ReclamosDetalle.as_view(), name='detalleReclamos'),
    path('editReclam/<pk>/',ReclamosEdit.as_view(), name='editReclamos'),
    path('deleteReclam/<pk>/',ReclamosDelete.as_view(), name='deleteReclamos'),

]
