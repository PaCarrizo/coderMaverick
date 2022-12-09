from django.urls import path
from .views import menu, pagblog, pagreclamos, pagrecomendaciones,post,BlogDelete,BlogEdit,RecomendacionList,RecomendacionDetalle,RecomendacionEdit,RecomendacionDelete

urlpatterns = [
    path('',menu, name='menu'),
    path('blog/',pagblog, name='blog'),
    path('reclamo/',pagreclamos, name='reclamo'),
    path('recomendacion/',pagrecomendaciones, name='recomendacion'),
    path('articulos/',post, name='post'),

    path('editBlog/<pk>/',BlogEdit.as_view(), name='editPost'),
    path('deleteBlog/<pk>/',BlogDelete.as_view(), name='deletePost'),

    path('listaReco/',RecomendacionList.as_view(), name='listRecomendacion'),
    path('detalleReco/<pk>/',RecomendacionDetalle.as_view(), name='detalleRecomendacion'),
    path('editReco/<pk>/',RecomendacionEdit.as_view(), name='editRecomendacion'),
    path('deleteReco/<pk>/',RecomendacionDelete.as_view(), name='deleteRecomendacion'),

]
