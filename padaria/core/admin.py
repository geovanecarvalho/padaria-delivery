from django.contrib import admin
from .models import ClientModel, ProductModel, SaleModel

admin.site.register(ClientModel)
admin.site.register(ProductModel)
admin.site.register(SaleModel)

