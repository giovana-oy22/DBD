from django.db import models

TAMANHO_PADRAO = 100

# RESTAURANTE
class Restaurante(models.Model):
    nome = models.CharField(max_length=TAMANHO_PADRAO)
    endereco = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome

# CLIENTES
class Cliente(models.Model):
    nome = models.CharField(
        max_length= TAMANHO_PADRAO,
        verbose_name= "Nome do Cliente",
        help_text ="Digite o nome completo do cliente"
    )
    rua = models.CharField(
        max_length=TAMANHO_PADRAO,
        verbose_name="Rua",
        help_text="Ex: Avenida Paulista"
    )
    numero = models.CharField(
        max_length=10,
        verbose_name="Número",
        help_text="Ex: 123 ou 123A"
    )
    cidade = models.CharField(
        max_length=TAMANHO_PADRAO,
        verbose_name="Cidade",
        help_text="Ex: São Paulo"
    )
    estado = models.CharField(
        max_length=TAMANHO_PADRAO,
        verbose_name="Estado",
        help_text="Ex: SP"
    )

    def __str__(self):
        return self.nome
    
    def endereco_completo(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"


# PRODUTOS
class Produto(models.Model):
    nome = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.restaurante.nome}"


# PEDIDOS
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"
    
    @property
    def total(self):
        return sum(
            item.quantidade * item.produto.preco
            for item in self.itempedido_set.all()
        )


# ITENS DO PEDIDO
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"