from django.db import models

class Item(models.Model):
    code = models.IntegerField(verbose_name='Артикул')
    name = models.CharField(max_length=30, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена') #max_degits - макс длинна/max_places - мамкс разряд