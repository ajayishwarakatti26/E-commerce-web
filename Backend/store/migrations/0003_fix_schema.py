from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_cart_cartitem"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                'ALTER TABLE store_product RENAME COLUMN "Categort_id" TO category_id;',
                'ALTER TABLE store_product RENAME COLUMN "Categort_at" TO created_at;',
                'ALTER TABLE store_orderitem RENAME COLUMN "Product_id" TO product_id;',
                'ALTER TABLE store_cartitem RENAME COLUMN "Product_id" TO product_id;',
                "ALTER TABLE store_categort RENAME TO store_category;",
            ],
            reverse_sql=[
                "ALTER TABLE store_category RENAME TO store_categort;",
                'ALTER TABLE store_product RENAME COLUMN category_id TO "Categort_id";',
                'ALTER TABLE store_product RENAME COLUMN created_at TO "Categort_at";',
                'ALTER TABLE store_orderitem RENAME COLUMN product_id TO "Product_id";',
                'ALTER TABLE store_cartitem RENAME COLUMN product_id TO "Product_id";',
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
