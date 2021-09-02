import json
import os
from datetime import datetime
from .models import Product, ProductCategory


from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title': 'GeekShop',
        'time': datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/good.json')
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'categories': categories,
        'products': products,
        # 'products': json.load(open(file_path, encoding='utf-8')),
    }

    return render(request, 'products/products.html', context)