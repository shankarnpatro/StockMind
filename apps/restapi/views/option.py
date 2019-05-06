from rest_framework import generics, status
# Option Views.
from rest_framework.response import Response
from django.utils import timezone

from apps.option.models import Option
from apps.restapi.serializers.option import OptionSerializer


class OptionAPIView(generics.ListAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

    def list(self, request, *args, **kwargs):
        if request.query_params.get('option_type') == 'BuyPE' or request.query_params.get('option_type') == 'BuyCE':
            option = Option.objects.filter(option_type=request.query_params.get('option_type'))
        else:
            option = Option.objects.all()
        return Response(OptionSerializer(option, many=True).data)


class OptionCreateAPIView(generics.CreateAPIView):
    serializer_class = OptionSerializer

    def post(self, request, *args, **kwargs):
        option = Option()
        option.date_time = timezone.now()
        option.symbol_name = request.data.get('symbol_name')
        option.option_type = request.data.get('option_type')
        option.buy_price = request.data.get('buy_price')
        option.target_price = request.data.get('target_price')
        option.achievement = request.data.get('achievement')
        option.save()
        return Response(OptionSerializer(option).data, status=status.HTTP_200_OK)


class OptionUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.all()

    def patch(self, request, *args, **kwargs):
        option_id = self.kwargs['pk']
        option = Option.objects.get(id=option_id)

        if option:
            option.date_time = timezone.now()
            if request.data.get('symbol_name') is not None:
                option.symbol_name = request.data.get('symbol_name')
            if request.data.get('option_type') is not None:
                option.option_type = request.data.get('option_type')
            # if request.data.get('date_time') is not None:
            #     option.date_time = request.data.get('date_time')
            if request.data.get('buy_price') is not None:
                option.buy_price = request.data.get('buy_price')
            if request.data.get('target_price') is not None:
                option.target_price = request.data.get('target_price')
            if request.data.get('achievement') is not None:
                option.achievement = request.data.get('achievement')
                option.save()
            return Response(OptionSerializer(option).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Option Not found"}, status=status.HTTP_400_BAD_REQUEST)


class OptionDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.all()

    def destroy(self, request, *args, **kwargs):
        option_id = self.kwargs['pk']
        option = Option.objects.get(id=option_id)
        option.delete()
        return Response({"message": "Option is deleted"}, status=status.HTTP_204_NO_CONTENT)
