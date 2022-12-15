from django.shortcuts import render, redirect
from .models import Product


def add_product(request):
    if request.method == "GET":
        return render(request, 'products/add.html')
    else:
        print(request.POST.get('title'))
        product = Product()
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.user = request.user
        product.save()
        return redirect('/')
