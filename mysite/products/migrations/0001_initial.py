# Generated by Django 5.0.7 on 2024-08-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductGender",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.TextField(blank=True, null=True)),
                ("gender", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "gender_table",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ProductTable",
            fields=[
                ("product_id", models.TextField(blank=True, null=True)),
                ("rank", models.FloatField(blank=True, null=True)),
                ("product_name", models.TextField(primary_key=True, serialize=False)),
                ("category", models.TextField(blank=True, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                ("image_url", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("color", models.TextField(blank=True, null=True)),
                ("size", models.TextField(blank=True, null=True)),
                ("platform", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "product_table",
                "managed": True,
            },
        ),
    ]