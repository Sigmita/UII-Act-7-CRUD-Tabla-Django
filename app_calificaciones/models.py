from django.db import models

class Calificacion(models.Model):
    # id_calificacion se crea automáticamente como el Primary Key si no lo especificas.
    # Si quieres un campo explícito con ese nombre y control, puedes hacerlo así,
    # pero el 'id' por defecto de Django es más común y automático.
    # id_calificacion = models.AutoField(primary_key=True) 

    id_usuario = models.IntegerField() # Asumo que es un ID numérico de otro sistema
    id_contenido = models.IntegerField() # Asumo que es un ID numérico de otro sistema
    tipo_contenido = models.CharField(max_length=50) # Por ejemplo: 'pelicula', 'serie', 'documental'
    puntuacion = models.IntegerField() # Por ejemplo: de 1 a 5 estrellas

    def __str__(self):
        return f'Calificación ID: {self.id} | Usuario: {self.id_usuario} | Contenido: {self.id_contenido} | Puntuación: {self.puntuacion}'