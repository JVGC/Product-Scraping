# Generated by Django 4.2.1 on 2023-06-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=100, unique=True)),
                ("product_name", models.CharField(max_length=200)),
                ("url", models.URLField()),
                ("image_url", models.URLField()),
                ("barcode", models.CharField(max_length=100)),
                ("brands", models.CharField(max_length=300)),
                ("packaging", models.CharField(max_length=500)),
                ("quantity", models.CharField(max_length=50)),
                ("categories", models.CharField(max_length=500)),
                ("imported_t", models.DateTimeField(verbose_name="imported_time")),
                (
                    "status",
                    models.CharField(
                        choices=[("DR", "Drafted"), ("IM", "Imported")],
                        default="IM",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
