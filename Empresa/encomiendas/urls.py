from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encomiendas/', views.listar_encomiendas, name='listar_encomiendas'),
    path('encomiendas/nueva/', views.nueva_encomienda, name='nueva_encomienda'),
]
