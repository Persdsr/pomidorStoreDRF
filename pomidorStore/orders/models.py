from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ManyToManyField(Product, related_name='order_product')
    account = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='order_account')