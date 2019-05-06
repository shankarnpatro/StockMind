from datetime import date

from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from apps.equity.models import Buy, Sell
from apps.restapi.serializers.equity import EquityBuySerializer, EquitySellSerializer


# Equity Buy Views.
class BuyListAPIView(generics.ListAPIView):
    serializer_class = EquityBuySerializer

    def get_queryset(self):
        return Buy.objects.all()


class BuyCreateAPIView(generics.CreateAPIView):
    serializer_class = EquityBuySerializer

    def post(self, request, *args, **kwargs):
        buy = Buy()
        buy.symbol_name = request.data.get('symbol_name')
        buy.time = timezone.now()
        buy.date = date.today()
        buy.buy_price = request.data.get('buy_price')
        buy.target_price = request.data.get('target_price')
        buy.achievement = request.data.get('achievement')
        buy.save()
        return Response(EquityBuySerializer(buy).data, status=status.HTTP_200_OK)


class BuyUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = EquityBuySerializer

    def get_queryset(self):
        return Buy.objects.all()

    def patch(self, request, *args, **kwargs):
        buy_id = self.kwargs['pk']
        buy = Buy.objects.get(id=buy_id)

        if buy:
            buy.time = timezone.now()
            buy.date = date.today()
            if request.data.get('symbol_name') is not None:
                buy.symbol_name = request.data.get('symbol_name')
            # if request.data.get('time') is not None:
            #     buy.time = request.data.get(timezone.now())
            if request.data.get('buy_price') is not None:
                buy.buy_price = request.data.get('buy_price')
            if request.data.get('target_price') is not None:
                buy.target_price = request.data.get('target_price')
            if request.data.get('achievement') is not None:
                buy.achievement = request.data.get('achievement')
                buy.save()
            return Response(EquityBuySerializer(buy).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Buy Not found"}, status=status.HTTP_400_BAD_REQUEST, )


class BuyDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = EquityBuySerializer

    def get_queryset(self):
        return Buy.objects.all()

    def destroy(self, request, *args, **kwargs):
        buy_id = self.kwargs['pk']
        buy = Buy.objects.get(id=buy_id)
        buy.delete()
        return Response({"message": "Buy is deleted"}, status=status.HTTP_204_NO_CONTENT)


# Equity Sell Views.
class SellListAPIView(generics.ListAPIView):
    serializer_class = EquitySellSerializer

    def get_queryset(self):
        return Sell.objects.all()


class SellCreateAPIView(generics.CreateAPIView):
    serializer_class = EquitySellSerializer

    def post(self, request, *args, **kwargs):
        sell = Sell()
        sell.time = timezone.now()
        sell.date = date.today()
        sell.symbol_name = request.data.get('symbol_name')
        sell.sell_price = request.data.get('sell_price')
        sell.target_price = request.data.get('target_price')
        sell.achievement = request.data.get('achievement')
        sell.save()
        return Response(EquitySellSerializer(sell).data, status=status.HTTP_200_OK)


class SellUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = EquitySellSerializer

    def get_queryset(self):
        return Sell.objects.all()

    def patch(self, request, *args, **kwargs):
        sell_id = self.kwargs['pk']
        sell = Sell.objects.get(id=sell_id)

        if sell:
            sell.time = timezone.now()
            sell.date = date.today()
            if request.data.get('symbol_name') is not None:
                sell.symbol_name = request.data.get('symbol_name')
            # if request.data.get('time') is not None:
            #     sell.time = request.data.get(timezone.now())
            if request.data.get('sell_price') is not None:
                sell.sell_price = request.data.get('sell_price')
            if request.data.get('target_price') is not None:
                sell.target_price = request.data.get('target_price')
            if request.data.get('achievement') is not None:
                sell.achievement = request.data.get('achievement')
                sell.save()
            return Response(EquityBuySerializer(sell).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Sell Not found"}, status=status.HTTP_400_BAD_REQUEST, )


class SellDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = EquitySellSerializer

    def get_queryset(self):
        return Sell.objects.all()

    def destroy(self, request, *args, **kwargs):
        sell_id = self.kwargs['pk']
        sell = Buy.objects.get(id=sell_id)
        sell.delete()
        return Response({"message": "Sell is deleted"}, status=status.HTTP_204_NO_CONTENT)
