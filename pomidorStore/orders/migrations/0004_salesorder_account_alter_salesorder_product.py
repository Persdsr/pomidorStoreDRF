# Generated by Django 4.1.2 on 2022-10-22 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0003_salesorder_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_account', to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='product',
            field=models.ManyToManyField(related_name='order_product', to='products.product'),
        ),
    ]