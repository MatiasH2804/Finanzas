from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('calculos/', views.calculos, name='calculos'),
    path('historial/', views.historial, name='historial'),
    path('categorias/', views.categorias, name='categorias'),
    path('resumen/', views.resumen, name='resumen'),
    path('configuracion/', views.configuracion, name='configuracion'),
]
