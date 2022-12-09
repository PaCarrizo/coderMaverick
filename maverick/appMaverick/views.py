from django.shortcuts import render
from django.http import HttpResponse
from appMaverick.models import Recomendacion,Post,Reclamos
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic.edit import DeleteView,UpdateView
from django.views.generic import ListView,DetailView

# Create your views here.

def menu(request):
    return render(request,'appMaverick/index.html')

#modulo que permite ingresar un reclamo
def pagreclamos(request):
    mensaje = "Nos contactaremos por su reclamo"
    if request.method == "POST":
            q_nombre = request.POST["queja-name"]
            q_email = request.POST["queja-email"]
            q_categoria = request.POST["queja-category"]
            q_nota = request.POST["queja-message"]
            obj = Reclamos(nombre=q_nombre, email=q_email,categoria=q_categoria,nota=q_nota)
            obj.save() 
            return render(request,'appMaverick/pagreclamos.html',{"mensaje":mensaje})    
    return render(request,'appMaverick/pagreclamos.html')

#modulo que permite ingresar una recomendacion
def pagrecomendaciones(request):
    mensaje = "Gracias por tu Recomendacion"
    if request.method == "POST":
            reco_nombre = request.POST["reco-name"]
            reco_correo = request.POST["reco-email"]
            reco_comida = request.POST["reco-category"]
            reco_comentario = request.POST["reco-message"]
            obj = Recomendacion(nombre=reco_nombre, correo=reco_correo,comida=reco_comida,comentario=reco_comentario)
            obj.save()        
            return render(request,'appMaverick/pagrecomendaciones.html',{"mensaje":mensaje})     
    return render(request,'appMaverick/pagrecomendaciones.html')     

#CRUD BLOG (post) *****************
#modulo que permite ingresar un post en el blog
def post(request):
    mensaje = "Gracias por contribuir con el BLOG"
    if request.method == "POST":
            p_nombre = request.POST["post-name"]
            p_articulo = request.POST["post-articulo"]
            p_autor = request.POST["post-autor"]
            p_imagen = request.POST["post-imagen"]
            obj = Post(nombre=p_nombre, articulo=p_articulo,autor=p_autor,imagen=p_imagen)
            obj.save() 
            return render(request,'appMaverick/formpost.html',{"mensaje":mensaje})    
    return render(request,'appMaverick/formpost.html')

#modulo que pemite visualizar los post con aplicacion de busqueda por nombre y articulo
def pagblog(request):
    entradas = Post.objects.all()
    queryset = request.GET.get("buscar")
    if queryset:
        entradas = Post.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(articulo__icontains  = queryset)
        ).distinct()
    return render(request,'appMaverick/pagblog.html',{"posteos":entradas})

class BlogEdit(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/' 
    #fields = ['nombre', 'articulo','autor','imagen']

class BlogDelete(DeleteView):
    model = Post
    success_url = '/blog/' 
           


#CRUD RECOMENDACION *****
class RecomendacionList(ListView):
    model = Recomendacion
    template_name = 'appMaverick/recomendaciones_list.html'

class RecomendacionDetalle(DetailView):
    model = Recomendacion
    template_name = 'appMaverick/recomendaciones_detalle.html'

class RecomendacionEdit(UpdateView):
    model = Recomendacion
    fields = '__all__'
    success_url = '/listaReco/' 
 
class RecomendacionDelete(DeleteView):
    model = Recomendacion
    success_url = '/listaReco/' 
   

   
#CRUD RECLAMOS *****
class ReclamosList(ListView):
    model = Reclamos
    template_name = 'appMaverick/reclamos_list.html'

class ReclamosDetalle(DetailView):
    model = Reclamos
    template_name = 'appMaverick/reclamos_detalle.html'

class ReclamosEdit(UpdateView):
    model = Reclamos
    fields = '__all__'
    success_url = '/listaReco/' 
 
class ReclamosDelete(DeleteView):
    model = Reclamos
    success_url = '/listaReco/' 