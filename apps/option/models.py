from django.db import models


# Create your models here.


class Option(models.Model):
    OPTION_TYPES = (
        ('BuyCE', 'BuyCE'),
        ('BuyPE', 'BuyPE')
    )
    symbol_name = models.CharField(max_length=20, blank=False)
    option_type = models.CharField(max_length=8, choices=OPTION_TYPES, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    buy_price = models.IntegerField(blank=False)
    target_price = models.IntegerField(blank=False)
    achievement = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.symbol_name + '-' + self.option_type

    class Meta:
        verbose_name = 'option'
        verbose_name_plural = 'options'
