from django.shortcuts import render, redirect, get_object_or_404
from .models import Calificacion

# Listar calificaciones
def index(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'listar_calificaciones.html', {'calificaciones': calificaciones})

# # Ver calificación (opcional)
# def ver_calificacion(request, id_calificacion):
#     calificacion = get_object_or_404(Calificacion, id=id_calificacion)
#     return render(request, 'ver_calificacion.html', {'calificacion': calificacion})

# Agregar calificación
def agregar_calificacion(request):
    if request.method == 'POST':
        id_usuario = request.POST['id_usuario']
        id_contenido = request.POST['id_contenido']
        tipo_contenido = request.POST['tipo_contenido']
        puntuacion = request.POST['puntuacion']
        Calificacion.objects.create(
            id_usuario=id_usuario,
            id_contenido=id_contenido,
            tipo_contenido=tipo_contenido,
            puntuacion=puntuacion
        )
        return redirect('inicio')
    return render(request, 'agregar_calificacion.html')

# Editar calificación
def editar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id=id_calificacion)
    if request.method == 'POST':
        calificacion.id_usuario = request.POST['id_usuario']
        calificacion.id_contenido = request.POST['id_contenido']
        calificacion.tipo_contenido = request.POST['tipo_contenido']
        calificacion.puntuacion = request.POST['puntuacion']
        calificacion.save()
        return redirect('inicio')
    return render(request, 'editar_calificacion.html', {'calificacion': calificacion})

# Borrar calificación
def borrar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id=id_calificacion)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('inicio')
    return render(request, 'borrar_calificacion.html', {'calificacion': calificacion})