from django.db import models


# Create your models here.


class Buy(models.Model):
    symbol_name = models.CharField(max_length=255, blank=True, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    buy_price = models.IntegerField(blank=False)
    target_price = models.IntegerField(blank=False)
    achievement = models.TextField()

    def __str__(self):
        return self.symbol_name

    class Meta:
        verbose_name = 'buy'
        verbose_name_plural = 'buys'


class Sell(models.Model):
    symbol_name = models.CharField(max_length=20, blank=True, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    sell_price = models.IntegerField(blank=False, )
    target_price = models.IntegerField(blank=False)
    achievement = models.TextField()

    def __str__(self):
        return self.symbol_name

    class Meta:
        verbose_name = 'sell'
        verbose_name_plural = 'sells'
