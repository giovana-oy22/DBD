from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos),          # página principal
    path('adicionar/', views.adicionar_produto),
]