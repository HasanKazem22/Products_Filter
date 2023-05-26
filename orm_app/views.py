from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    warranty = Warranty.objects.all()
    filter_price = Filter_Price.objects.all()

    categories_id = request.GET.get('categories')
    brands_id = request.GET.get('brands')
    warranty_id = request.GET.get('warranty')
    price_id = request.GET.get('price')

    if categories_id:
        products = Product.objects.filter(categories = categories_id)
    elif brands_id:
        products = Product.objects.filter(brands = brands_id)
    elif warranty_id:
        products = Product.objects.filter(warranty = warranty_id)
    elif price_id:
        products = Product.objects.filter(filter_price = price_id)
    else:
        products = Product.objects.all()

    context = {
        'products' : products,
        'categories': categories,
        'brands': brands,
        'warranty': warranty,
        'filter_price': filter_price
        }
    return render(request, 'index.html', context)