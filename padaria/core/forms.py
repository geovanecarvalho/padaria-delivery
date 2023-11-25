from django.forms import ModelForm
from django import forms
from .models import ProductModel, SaleModel, ClientModel

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ["image","name", "amount", "value", "description"]

        widgets = {
            "image": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"URL da Imagem"}),
            "name": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Nome do produto"}),
            "amount": forms.NumberInput(attrs={"class":"form-control border border-dark", "placeholder":"Quantidade"}),
            "value": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Valor unitário R$"}),
            "description": forms.Textarea(attrs={"class":"form-control border border-dark", "placeholder":"Descrição"}),
        } 
        

class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ["first_name","last_name","date_of_birth","cpf","phone_number", "address" ] 


        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Nome"}),
            "last_name": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Sobrenome"}),
            "date_of_birth": forms.DateInput(attrs={"class":"form-control border border-dark", "placeholder":"Data de nascimento"}),
            "cpf": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Cpf"}),
            "phone_number": forms.TextInput(attrs={"class":"form-control border border-dark", "placeholder":"Telefone"}),
            "address": forms.Textarea(attrs={"class":"form-control border border-dark", "placeholder":"Endereço"}),
        } 

class SaleForm(ModelForm):
    class Meta:
        model = SaleModel
        fields = ["order_number","amount_buy", "client", "product"] 

        widgets = {
            
            "client": forms.Select(attrs={"class":"form-select border border-dark", "placeholder":"Nome do produto"}),
            "amount_buy": forms.NumberInput(attrs={"class":"form-control border border-dark", "placeholder":"Quantidade"}),
        } 