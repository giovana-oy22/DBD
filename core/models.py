from django.db import models

# CLIENTES
class Cliente(models.Model):
    nome = models.TextField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome


# PRODUTOS
class Produto(models.Model):
    nome = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


# PEDIDOS
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"


# ITENS DO PEDIDO
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} ({self.quantidade})"