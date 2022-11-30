from django.shortcuts import render
from django.http import HttpResponse
from appMaverick.models import Recomendacion,Post,Reclamos

# Create your views here.

def menu(request):
    return render(request,'appMaverick/index.html')

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


def leftside(request):
    posteos = Post.objects.all()
    return render(request,'appMaverick/left-sidebar.html',{"posteos":posteos})

def noside(request):
    mensaje = "Nos contactaremos por su reclamo"
    if request.method == "POST":
            q_nombre = request.POST["queja-name"]
            q_email = request.POST["queja-email"]
            q_categoria = request.POST["queja-category"]
            q_nota = request.POST["queja-message"]
            obj = Reclamos(nombre=q_nombre, email=q_email,categoria=q_categoria,nota=q_nota)
            obj.save() 
            return render(request,'appMaverick/no-sidebar.html',{"mensaje":mensaje})    
    return render(request,'appMaverick/no-sidebar.html')

def rightside(request):
    mensaje = "Gracias por tu Recomendacion"
    if request.method == "POST":
            reco_nombre = request.POST["reco-name"]
            reco_correo = request.POST["reco-email"]
            reco_comida = request.POST["reco-category"]
            reco_comentario = request.POST["reco-message"]
            obj = Recomendacion(nombre=reco_nombre, correo=reco_correo,comida=reco_comida,comentario=reco_comentario)
            obj.save()        
            return render(request,'appMaverick/right-sidebar.html',{"mensaje":mensaje})     
    return render(request,'appMaverick/right-sidebar.html')            