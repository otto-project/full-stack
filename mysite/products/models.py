# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models
from django.db.models import Subquery


class ProductTable(models.Model):
    product_id = models.TextField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    product_name = models.TextField(primary_key=True)
    category = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)

    class Meta:
        managed = not settings.TESTING  # 테스트 환경에서만 managed = True
        db_table = 'product_table'

    @staticmethod
    def get_product_order_by_rank(platform, category):
        return ProductTable.objects.filter(platform=platform, category=category).order_by('rank')

    @staticmethod
    def get_product_filter_by_gender(platform, category, gender):
        gender_product_names = ProductGender.objects.filter(gender=gender).values('product_name')
        return ProductTable.objects.filter(
            platform=platform,
            category=category,
            product_name__in=Subquery(gender_product_names)
        ).order_by('rank')


class ProductGender(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)

    class Meta:
        managed = not settings.TESTING
        db_table = 'gender_table'
