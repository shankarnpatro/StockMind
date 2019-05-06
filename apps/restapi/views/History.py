from rest_framework import generics

from apps.equity.models import Buy, Sell
from apps.option.models import Option
from apps.restapi.serializers.equity import EquityBuySerializer
from apps.restapi.serializers.option import OptionSerializer


class EquityBuyHistoryListAPIView(generics.ListAPIView):
    serializer_class = EquityBuySerializer

    def get_queryset(self):
        if self.request.GET != {}:
            offset = 0
            if 'offset' in self.request.GET:
                offset = int(self.request.GET['offset'])

            limit = 5
            if 'limit' in self.request.GET:
                limit = int(self.request.GET['limit'])

            return Buy.objects.all()[offset:limit]

        return Buy.objects.all()


class EquitySellHistoryListAPIView(generics.ListAPIView):
    serializer_class = EquityBuySerializer

    def get_queryset(self):
        if self.request.GET != {}:
            offset = 0
            if 'offset' in self.request.GET:
                offset = int(self.request.GET['offset'])

            limit = 5
            if 'limit' in self.request.GET:
                limit = int(self.request.GET['limit'])

            return Sell.objects.all()[offset:limit]

        return Sell.objects.all()


class OptionBuyCEHistoryListAPIView(generics.ListAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        if self.request.GET != {}:
            offset = 0
            if 'offset' in self.request.GET:
                offset = int(self.request.GET['offset'])

            limit = 5
            if 'limit' in self.request.GET:
                limit = int(self.request.GET['limit'])

            return Option.objects.all().filter(option_type='BuyCE')[offset:limit]

        return Option.objects.all().filter(option_type='BuyCE')


class OptionBuyPEHistoryListAPIView(generics.ListAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        if self.request.GET != {}:
            offset = 0
            if 'offset' in self.request.GET:
                offset = int(self.request.GET['offset'])

            limit = 5
            if 'limit' in self.request.GET:
                limit = int(self.request.GET['limit'])

            return Option.objects.all().filter(option_type='BuyC')[offset:limit]

        return Option.objects.all().filter(option_type='BuyPE')
