from django.db import models

# Create your models here.
class Pregunta(models.Model):
	pregunta_text = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField("fecha de publicacion")
	def __str__(self):
		return self.pregunta_text
	
class Eleccion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	texto_eleccion = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
	def __str__(self):
		return self.texto_eleccion
