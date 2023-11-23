from django.forms import ModelForm
from django import forms
from .models import ProductModel, SaleModel, ClientModel

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ["image","name", "amount", "value", "description"]

        widgets = {
            "image": forms.TextInput(attrs={"class":"form-control", "placeholder":"URL da Imagem"}),
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Nome do produto"}),
            "amount": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Quantidade"}),
            "value": forms.TextInput(attrs={"class":"form-control", "placeholder":"Valor R$"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Descrição"}),
        } 
        

class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ["first_name","last_name","date_of_birth","cpf","phone_number", "address" ] 


class SaleForm(ModelForm):
    class Meta:
        model = SaleModel()
        fields = ["order_number","amount_buy", "client", "product"] 