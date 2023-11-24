from django.shortcuts import render
from .models import ProductModel, SaleModel
from .forms import ProductForm, ClientForm, SaleForm
import secrets

def home(request):
    obj = ProductModel.objects.all()
    
    return render(request, 'home.html', {'products': obj})

def product_list(request):
    obj = ProductModel.objects.all()
    return render(request, 'product_list.html', {'products': obj})

def detail(request, pk):
    obj = ProductModel.objects.get(pk=pk)
    sale = SaleForm()
    
    

    if request.method == "POST":
    
        client = request.POST.get('client')
        amount_buy = request.POST.get('amount_buy')
        if obj.amount > int(amount_buy):
            quantidade = obj.amount - int(amount_buy)
            obj.amount = quantidade
            obj.save()
         
         
            sale_model = SaleModel()

            sale_model.product_id = pk
            sale_model.client_id = client
            sale_model.amount_buy = amount_buy
            sale_model.order_number = "%04d"% int(obj.pk)
            valor = float(obj.value)
            quantidade = int(sale_model.amount_buy)
            sale_model.total = quantidade * valor

            sale_model.save()
            
            
            
        

    return render(request, 'detail.html', {'products': obj, 'sale':sale})


def register_customer(request):
    form = ProductForm()

    return render(request, 'register_product.html', {"form": form})

def register_client(request):
    form = ClientForm()
    return render(request, 'register_client.html', {"form": form})