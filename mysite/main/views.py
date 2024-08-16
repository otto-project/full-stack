from django.shortcuts import redirect
from django.shortcuts import render
from products.models import ProductTable
from users.models import UserMLResult


def index(request):
    return redirect('main_platform', platform='musinsa')


def main_platform(request, platform):
    if request.user.is_authenticated:
        gender = request.user.gender
        top = ProductTable.get_product_filter_by_gender(platform, 'top', gender)[:10]
        bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', gender)[:10]

        # 사용자에 대한 ML 결과 가져오기
        ml_results = UserMLResult.objects.filter(user=request.user).select_related('product')

        # 제품별로 학습 결과 매핑
        top_results = {result.product.product_name: result for result in ml_results if result.product.category == 'top'}
        bottom_results = {result.product.product_name: result for result in ml_results if
                          result.product.category == 'bottom'}

        # top과 bottom 리스트에 학습 결과를 추가
        top_with_results = []
        for product in top:
            result = top_results.get(product.product_name)
            top_with_results.append({
                'product': product,
                'size': result.size if result else product.size,
                'score': convert_to_score(result.score) if result else None,
            })

        bottom_with_results = []
        for product in bottom:
            result = bottom_results.get(product.product_name)
            bottom_with_results.append({
                'product': product,
                'size': result.size if result else product.size,
                'score': convert_to_score(result.score) if result else None,
            })

        return render(request, 'main/logged_in.html', {
            'top': top_with_results,
            'bottom': bottom_with_results,
            'gender': gender
        })
    else:
        women_top = ProductTable.get_product_filter_by_gender(platform, 'top', 'female')[:10]
        women_bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', 'female')[:10]
        men_top = ProductTable.get_product_filter_by_gender(platform, 'top', 'male')[:10]
        men_bottom = ProductTable.get_product_filter_by_gender(platform, 'bottom', 'male')[:10]
        return render(request, 'main/logged_out.html',
                      {'women_top': women_top, 'women_bottom': women_bottom, 'men_top': men_top,
                       'men_bottom': men_bottom})


def convert_to_score(percentage):
    # 0% ~ 100%의 수치를 50 ~ 100으로 변환
    min_score = 50
    max_score = 100

    # 비율을 점수로 변환
    score = min_score + (percentage * (max_score - min_score))
    return round(score, 2)
