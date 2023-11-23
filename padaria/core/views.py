from django.shortcuts import render
from .models import ProductModel
from .forms import ProductForm

def home(request):
    obj = ProductModel.objects.all()
    
    return render(request, 'home.html', {'products': obj})


def detail(request, pk):
    obj = ProductModel.objects.get(pk=pk)

    return render(request, 'detail.html', {'products': obj})


def register_customer(request):
    form = ProductForm()

    return render(request, 'register.html', {"form": form})