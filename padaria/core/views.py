from django.shortcuts import render
from .models import ProductModel

def home(request):
    obj = ProductModel.objects.all()
    
    return render(request, 'home.html', {'products': obj})


def detail(request, pk):
    obj = ProductModel.objects.get(pk=pk)

    return render(request, 'detail.html', {'products': obj})