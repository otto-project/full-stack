from django.shortcuts import render

from products.models import ProductTable


# Create your views here.
def index(request):
    return render(request, "main/main.html")


def main_musinsa(request):
    top = ProductTable.get_product_order_by_rank('musinsa', 'top')[:10]
    bottom = ProductTable.get_product_order_by_rank('musinsa', 'bottom')[:10]
    return render(request, "main/main.html", {'top': top, 'bottom': bottom})


def main_29cm(request):
    top = ProductTable.get_product_order_by_rank('29cm', 'top')[:10]
    bottom = ProductTable.get_product_order_by_rank('29cm', 'bottom')[:10]
    return render(request, "main/main.html", {'top': top, 'bottom': bottom})


def main_zigzag(request):
    top = ProductTable.get_product_order_by_rank('zigzag', 'top')[:10]
    bottom = ProductTable.get_product_order_by_rank('zigzag', 'bottom')[:10]
    return render(request, "main/main.html", {'top': top, 'bottom': bottom})
