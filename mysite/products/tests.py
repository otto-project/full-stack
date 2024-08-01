from django.test import TestCase

from .models import ProductTable


# Create your tests here.

class ProductTableTest(TestCase):

    def test_get_product_order_by_rank(self):
        products = ProductTable.get_product_order_by_rank('musinsa', 'top')
        print(products)
