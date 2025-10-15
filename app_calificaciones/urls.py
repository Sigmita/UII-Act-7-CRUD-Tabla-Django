from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    # path('<int:id_calificacion>', views.ver_calificacion, name='ver_calificacion'), # Opcional si quieres una vista de detalle
    path('agregar/', views.agregar_calificacion, name='agregar_calificacion'),
    path('editar/<int:id_calificacion>/', views.editar_calificacion, name='editar_calificacion'),
    path('borrar/<int:id_calificacion>/', views.borrar_calificacion, name='borrar_calificacion'),
]