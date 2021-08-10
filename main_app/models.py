from django.db import models


class Product(models.Model):
    stock_keeping_unit = models.CharField(max_length=30,
                                          verbose_name='SKU',
                                          unique=True,
                                          null=False)
    title = models.CharField(max_length=200,
                             verbose_name='Наименование',
                             null=False)
    product_type = models.ForeignKey('main_app.ProductType',
                                     on_delete=models.CASCADE,
                                     verbose_name='Тип',
                                     default=None,
                                     null=False)
    price = models.FloatField(verbose_name='Стоимость')

    def __str__(self):
        st = f'{self.stock_keeping_unit} | {self.title} | {self.price} руб.'
        return st


class ProductType(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        st = f'{self.title}'
        return st


class Purchase(models.Model):
    """Покупка"""
    product = models.ForeignKey('main_app.Product',
                                verbose_name='Продукт',
                                default=None,
                                null=False,
                                on_delete=models.DO_NOTHING)

    email = models.EmailField(verbose_name='e-mail',
                              default='',
                              null=False)
