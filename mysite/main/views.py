from django.shortcuts import redirect
from django.shortcuts import render
from products.models import ProductTable


# Create your views here.
def index(request):
    return redirect('main_platform', platform='musinsa')


def main_platform(request, platform='musinsa'):
    if request.user.is_authenticated:
        gender = request.user.gender
        top = ProductTable.get_product_filter_by_gender(platform, 'top', gender)[:10]
        bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', gender)[:10]
        return render(request, 'main/logged_in.html', {'top': top, 'bottom': bottom, 'gender': gender})
    else:
        women_top = ProductTable.get_product_filter_by_gender(platform, 'top', 'women')[:10]
        women_bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', 'women')[:10]
        men_top = ProductTable.get_product_filter_by_gender(platform, 'top', 'men')[:10]
        men_bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', 'men')[:10]
        return render(request, 'main/logged_out.html',
                      {'women_top': women_top, 'women_bottom': women_bottom, 'men_top': men_top,
                       'men_bottom': men_bottom})
