# Generated by Django 5.1.5 on 2025-01-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
    ]
