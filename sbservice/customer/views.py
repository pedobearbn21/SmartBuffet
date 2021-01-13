from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from customer.models import TablestableInStore , Tabledailydate , Meats , Orders
from rest_framework import generics, viewsets
from customer.serializers import OrderSerializers, MeatSerializers, TableDailySerializers, OrderManySerializers
from django.utils import timezone

# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializers

class OrderIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    lookup_field = 'id'
    serializer_class = OrderSerializers

class OrderPost(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializers

class MeatView(generics.ListCreateAPIView):
    queryset = Meats.objects.all()
    serializer_class = MeatSerializers

class MeatIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meats.objects.all()
    lookup_field = 'id'
    serializer_class = MeatSerializers

class Search(generics.ListAPIView):
    serializer_class = MeatSerializers
    lookup_url_kwarg = 'type'

    def get_queryset(self):
        type_id = self.kwargs.get(self.lookup_url_kwarg)
        meatlist = Meats.objects.filter(type=type_id)
        return meatlist

class GraphTotalCustomer(generics.ListAPIView):
    serializer_class = TableDailySerializers
    
    def get_queryset(self):
        total = Tabledailydate.objects.filter(table_open_time__date = timezone.now())
        return total