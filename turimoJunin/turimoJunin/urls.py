"""turimoJunin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import homeView, destinoView, getDistritos, getDestinos, lugarTuristicoView, getCoordenadas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('destinos/', destinoView, name='destinos'),
    path('destinos/<str:nombre>/', lugarTuristicoView),
    path('api/distritos/', getDistritos, name='api_distritos'),
    path('api/destinos/', getDestinos, name='api_destinos'),
    path('api/coordenadas/<str:nombre>/', getCoordenadas),
]
