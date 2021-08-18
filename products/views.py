from datetime import datetime

from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'time': datetime.now(),
    }


    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6900,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'
            }
        ]
    }

    return render(request, 'products/products.html', context)