from django.shortcuts import render

# Create your views here.

def detalle(request, pregunta_id):
	return HttpResponse("Estás viendo una pregunta %s" % pregunta_id)

def resultados(request, pregunta_id):
	response = "Estás viendo las respuestas de la pregunta %s" 
	return HttpResponse(response % pregunta_id)

def votos(request, pregunta_id):
	return HttpResponse("Estás votando sobre la pregunta %s" % pregunta_id)