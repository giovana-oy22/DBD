"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from core.views import (
    home_web,
    criar_pedido,
    lista_produtos,
    lista_restaurantes,
    lista_pedidos,
    restaurantes_proximos,
    restaurantes_proximos_cliente,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_web, name='painel'),
    path('pedidos/criar/', criar_pedido, name='criar_pedido'),
    path('api/produtos/', lista_produtos),
    path('api/restaurantes/', lista_restaurantes),
    path('api/pedidos/', lista_pedidos),
    path('api/restaurantes-proximos/', restaurantes_proximos),
    path('api/restaurantes-proximos-cliente/', restaurantes_proximos_cliente),
    path('produtos/', include('core.urls')),
]
