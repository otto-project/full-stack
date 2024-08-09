from django.test import TestCase

from .models import ProductGender
from .models import ProductTable


# Create your tests here.

class ProductTableTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # ProductTable 데이터 생성
        ProductTable.objects.create(
            product_name='Product A', platform='musinsa', category='top', rank=1.0
        )
        ProductTable.objects.create(
            product_name='Product B', platform='29cm', category='top', rank=2.0
        )
        ProductTable.objects.create(
            product_name='Product C', platform='zigzag', category='bottom', rank=3.0
        )

        # ProductGender 데이터 생성
        ProductGender.objects.create(
            product_name='Product A', gender='male'
        )
        ProductGender.objects.create(
            product_name='Product B', gender='female'
        )
        ProductGender.objects.create(
            product_name='Product B', gender='male'
        )

    def test_get_product_filter_by_gender_male(self):
        products = ProductTable.get_product_filter_by_gender(platform='musinsa', category='top', gender='male')
        self.assertEqual(len(products), 1)
        self.assertIn('Product A', [product.product_name for product in products])

    def test_get_product_filter_by_gender_female(self):
        products = ProductTable.get_product_filter_by_gender(platform='29cm', category='top', gender='female')
        self.assertEqual(len(products), 1)
        self.assertIn('Product B', [product.product_name for product in products])

    def test_get_product_filter_by_gender_zigzag(self):
        products = ProductTable.get_product_filter_by_gender(platform='zigzag', category='bottom', gender='female')
        self.assertEqual(len(products), 0)
