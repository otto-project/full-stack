from django.shortcuts import redirect
from django.shortcuts import render
from products.models import ProductTable


# Create your views here.
def index(request):
    return redirect('main_platform', platform='musinsa')


def main_platform(request, platform='musinsa'):
    if request.user.is_authenticated:
        html = 'main/logged_in.html'
    else:
        html = 'main/logged_out.html'
    top = ProductTable.get_product_order_by_rank(platform, 'top')[:10]
    bottom = ProductTable.get_product_order_by_rank(platform, 'bottom')[:10]
    return render(request, html, {'top': top, 'bottom': bottom})
