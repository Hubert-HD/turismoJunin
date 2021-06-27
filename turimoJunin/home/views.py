from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def homeView(request):
  context ={
    "recomendados" : [
      {
        "imagen": "http://4.bp.blogspot.com/_03HTyDMRosQ/TRuQPezxK4I/AAAAAAAAAFo/PdmL8Uastyo/s1600/langui.jpg",
        "nombre": "Laguna De Langui Layo",
        "provincia": "Canas",
        "categoria": "Sitio natural",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      }
    ]
  }
  return render(request, 'pages/home.html', context)

def destinoView(request):
  context ={
    "recomendados" : {
      "naturales" : [
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        }
      ],
      "culturales" : [
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        }
      ],
      "realizaciones" : [
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        },
        {
          "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
          "nombre": "nombre django",
          "provincia": "provincia django",
          "categoria": "categoria django",
          "corazones": 0,
        }
      ]
    }
  }
  return render(request, 'pages/destinos.html', context)

def lugarTuristicoView(request, nombre):
  context = {
    "imagen": "http://4.bp.blogspot.com/_03HTyDMRosQ/TRuQPezxK4I/AAAAAAAAAFo/PdmL8Uastyo/s1600/langui.jpg",
    "nombre": nombre,
    "subtitulo": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas at enim ligula. Quisque nec leo et eros pharetra venenatis.",
    "provincia": "Canas",
    "distrito": "Langui",
    "categoria": "Sitio Natural",
    "latitud": -14.499080282861806,
    "longuitud": -71.16602045996092,
    "corazones": 0,
    "parrafos": [
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam sagittis, ipsueu efficitur molestie, dui lacus rutrum lorem, quis tincidunt mi elit sit amet nisi. Donec cursus orci in enim vehicula, condimentum venenatis mi consectetur. Donec pretium metus et tincidunt tincidunt ipsum dolor sit amet, consectetur adipiscing elit. Nullam sagittis, ipsueu efficitur molestie, dui lacus rutrum lorem, quis tincidunt mi elit sit amet nisi. Donec cursus orci in enim vehicula, condimentum venenatis mi consectetur. Donec pretium metus et tincidunt tincidunt.", "Aliquam egestas justo at dolor faucibus, nec tempus nulla ultrices. Donec sodales ante mi, eu posuere nibh dictum eu. Proin iaculis congue ultricies. Proin vel dui in eros fermentum pellentesque."
    ],
    "recomendados" : [
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      },
      {
        "imagen": "http://127.0.0.1:8000/static/img/natural.jpg",
        "nombre": "nombre django",
        "provincia": "provincia django",
        "categoria": "categoria django",
        "corazones": 0,
      }
    ]
  };

  return render(request, 'pages/lugar.html', context)

def getDistritos(request):
  data = ["Distrito 1.1", "Distrito 1.2", "Distrito 1.3", "Distrito 1.4", "Distrito 1.5", "Distrito 1.6"]
  return JsonResponse(data, safe=False)

def getDestinos(request):
  data = [
    {
      "id": "1",
      "link": "https://myanimelist.net/images/characters/16/309714.jpg",
      "nombre": "Nombre 1",
      "provincia": "provincia 1",
      "distrito": "distrito 1",
      "categoria": "categoria 1",
      "corazones": "75"
    },
    {
      "id": "2",
      "link": "https://myanimelist.net/images/characters/16/309714.jpg",
      "nombre": "Nombre 1",
      "provincia": "provincia 1",
      "distrito": "distrito 1",
      "categoria": "categoria 1",
      "corazones": "123"
    },
    {
      "id": "3",
      "link": "https://myanimelist.net/images/characters/16/309714.jpg",
      "nombre": "Nombre 3",
      "provincia": "provincia 1",
      "distrito": "distrito 1",
      "categoria": "categoria 1",
      "corazones": "205"
    },
    {
      "id": "2",
      "link": "https://myanimelist.net/images/characters/16/309714.jpg",
      "nombre": "Nombre 1",
      "provincia": "provincia 1",
      "distrito": "distrito 1",
      "categoria": "categoria 1",
      "corazones": "123"
    },
    {
      "id": "3",
      "link": "https://myanimelist.net/images/characters/16/309714.jpg",
      "nombre": "Nombre 3",
      "provincia": "provincia 1",
      "distrito": "distrito 1",
      "categoria": "categoria 1",
      "corazones": "205"
    }
  ]
  return JsonResponse(data, safe=False)

def getCoordenadas(request, nombre):

  data = [
    {
      "latitud": -14.499080282861806,
      "longuitud": -71.16602045996092,
    }
  ]
  return JsonResponse(data, safe=False)