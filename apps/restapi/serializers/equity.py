from rest_framework import serializers

from apps.equity.models import Buy, Sell


class EquityBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'
        read_only_fields = ('time', 'date')


class EquitySellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'
        read_only_fields = ('time', 'date')
