from django.shortcuts import render

from products.models import ProductTable


# Create your views here.
def index(request):
    products = ProductTable.objects.all()[:10]
    return render(request, "main/main.html", {'products': products})


def musinsa_main(request):
    return render(request, "main/musinsa_main.html")
