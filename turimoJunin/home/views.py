from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Provincia, Categoria, Distrito, Recurso, Coordenadas

# Create your views here.
def homeView(request):
  recomendados = []
  for recurso in Recurso.objects.all().order_by('nombre')[:5]:
    recomendados.append({
      'id': recurso.id,
      'imagen': recurso.image_URL,
      'nombre': recurso.nombre,
      'provincia': recurso.distrito_id.nombre,
      'categoria': recurso.categoria_id.nombre,
      'corazones': 0
    })
  context ={
    "recomendados" : recomendados
  }
  return render(request, 'pages/home.html', context)

def destinoView(request):
  provincias = []
  categorias = []
  naturales = []
  culturales = []
  realizaciones = []
  for provincia in Provincia.objects.all():
    provincias.append(provincia.nombre)
  for categoria in Categoria.objects.all():
    categorias.append(categoria.nombre)
  for recurso in Recurso.objects.all().order_by('nombre')[:3]:
    r = {
      'imagen': recurso.image_URL,
      'nombre': recurso.nombre,
      'provincia': recurso.distrito_id.nombre,
      'categoria': recurso.categoria_id.nombre,
      'corazones': 0
    }
    naturales.append(r)
    culturales.append(r)
    realizaciones.append(r)

  context ={
    "provincias": provincias,
    "categorias": categorias,
    "recomendados" : {
      "naturales" : naturales,
      "culturales" : culturales,
      "realizaciones" : realizaciones
    }
  }
  return render(request, 'pages/destinos.html', context)

def lugarTuristicoView(request, nombre):
  if(Recurso.objects.filter(nombre=nombre).exists()):
    recomendados = []
    for recurso in Recurso.objects.all().order_by('nombre')[:5]:
      recomendados.append({
        'id': recurso.id,
        'imagen': recurso.image_URL,
        'nombre': recurso.nombre,
        'provincia': recurso.distrito_id.provincia_id.nombre,
        'categoria': recurso.categoria_id.nombre,
        'corazones': 0
      })
    recurso = Recurso.objects.filter(nombre=nombre).get()
    context = {
      "imagen": recurso.image_URL,
      "nombre": recurso.nombre,
      "subtitulo": recurso.subtitulo,
      "provincia": recurso.distrito_id.provincia_id.nombre,
      "distrito": recurso.distrito_id.nombre,
      "categoria": recurso.categoria_id.nombre,
      "corazones": 0,
      "parrafos": [ recurso.descripcion ],
      "recomendados" : recomendados
    };
    return render(request, 'pages/lugar.html', context)
  else:
    return render(request, 'no_econtrado.html')

def getDistritos(request):
  provincia = request.GET['provincia']
  data=[]
  for distrito in Distrito.objects.filter(provincia_id__nombre=provincia):
    data.append(distrito.nombre)
  return JsonResponse(data, safe=False)

def getDestinos(request):
  provincia = request.GET["provincia"];
  distrito = request.GET["distrito"];
  categoria = request.GET["categoria"];

  recursos = Recurso.objects.all()

  if Provincia.objects.filter(nombre=provincia).exists():
    recursos = recursos & Recurso.objects.filter(distrito_id__provincia_id__nombre=provincia)

  if Distrito.objects.filter(nombre=distrito).exists():
    recursos = recursos & Recurso.objects.filter(distrito_id__nombre=distrito)

  if Categoria.objects.filter(nombre=categoria).exists():
    recursos = recursos & Recurso.objects.filter(categoria_id__nombre=categoria)

  data=[]
  for recurso in recursos:
    data.append({
      'id': recurso.id,
      'link': recurso.image_URL,
      'nombre': recurso.nombre,
      'provincia': recurso.distrito_id.provincia_id.nombre,
      'distrito': recurso.distrito_id.nombre,
      'categoria': recurso.categoria_id.nombre,
      'corazones': 0
    })

  return JsonResponse(data, safe=False)

def getCoordenadas(request):
  nombre = request.GET["nombre"];
  data = {
    "latitud": 0,
    "longuitud": 0,
  }
  if Coordenadas.objects.filter(recurso_id__nombre=nombre).exists():
    coordenada = Coordenadas.objects.filter(recurso_id__nombre=nombre).get()
    data["latitud"] = coordenada.longitud        #to do:
    data["longuitud"] = coordenada.latitud     #to do:
  return JsonResponse(data, safe=False)

def getRecomendaciones(request):
  provincia = request.GET["provincia"];
  distrito = request.GET["distrito"];
  categoria = request.GET["categoria"];

  recursos = Recurso.objects.all().order_by('nombre')[:5]

  data=[]

  for recurso in recursos:
    data.append({
      'link': recurso.image_URL,
      'nombre': recurso.nombre,
      'provincia': recurso.distrito_id.provincia_id.nombre,
      'distrito': recurso.distrito_id.nombre,
      'categoria': recurso.categoria_id.nombre,
      'corazones': 0
    })

  return JsonResponse(data, safe=False)