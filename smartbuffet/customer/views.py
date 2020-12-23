from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import tablestableinstore , tabeldailydate , meat , order
from rest_framework import generics
from .serializers import OrderSerializers

# Create your views here.
class MyView(View):

    def get(self, request, *args, **kwargs):
        meatmeat = order.objects.get(pk=1)
        meatmeats = meatmeat.meat.all()
        print(meatmeats)
        return HttpResponse(meatmeats)

class OrderView(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializers