from django.db import models
from api.fields import WEBPField


class Product(models.Model):
    STATUS_CHOICE = (
        (1, 'В наличии'),
        (2, 'Под заказ'),
        (3, 'Ожидается поступление'),
        (4, 'Нет в наличии'),
        (5, 'Не производится')
    )

    title = models.CharField(max_length=255)
    sku = models.IntegerField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE)
    image = WEBPField(upload_to='media/images/product')

    def __str__(self):
        return self.title
