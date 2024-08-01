# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
        managed = False
        db_table = 'product_table'
