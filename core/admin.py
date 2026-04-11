from django.contrib import admin
from .models import Restaurante, Produto, Cliente, Pedido, ItemPedido

admin.site.register(Produto)
admin.site.register(Restaurante)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)