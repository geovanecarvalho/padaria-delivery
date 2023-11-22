from django.db import models


# Tabela de Clientes
class ClientModel(models.Model):
    first_name = models.CharField("Nome", max_length=80)
    last_name = models.CharField("Sobrenome", max_length=200)
    date_of_birth = models.DateField("Data de nascimento")
    cpf = models.CharField("CPF", max_length=11)
    phone_number = models.CharField("Número de telefone", max_length=11)
    address = models.CharField("Endereço", max_length=254)
    created_at = models.DateTimeField("Criado em",auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['first_name']

    def __str__(self):
        return self.first_name


# Tabela de Produtos
class ProductModel(models.Model):
    image = models.URLField("Imagem")
    name = models.CharField("Nome", max_length=254)
    amount = models.PositiveIntegerField("Quantidade")
    value = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    description = models.TextField("Descrição", blank=True)
    created_at = models.DateTimeField("Criado em",auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)


    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['id']


    def __str__(self):
        return self.name


# Tabela de Vendas
class SaleModel(models.Model):
    order_number = models.CharField("Número de Pedido", max_length=4)
    amount_buy = models.PositiveIntegerField("Quantidade")
    client = models.ForeignKey(ClientModel, 
                               verbose_name="Cliente", 
                               on_delete=models.CASCADE, 
                               related_name="ordereds", 
                               null=True, 
                               blank=True)
    product = models.ForeignKey(ProductModel, 
                                verbose_name="Produto", 
                                on_delete=models.CASCADE, 
                                related_name="ordereds", 
                                null=True, 
                                blank=True)
    sale_created_at = models.DateTimeField("Vendido em",auto_now_add=True)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['order_number']

    def __str__(self):
        return "Número de pedido: " + self.order_number
    
    

