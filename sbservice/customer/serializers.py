from django.db import models
from rest_framework import serializers
from django.core.serializers import serialize

from customer.models import TablestableInStore , Tabledailydate , Meats , Orders


class TableDailySerializers(serializers.ModelSerializer):
    class Meta :
        model = Tabledailydate
        fields = '__all__'

class MeatSerializers(serializers.ModelSerializer):
    # meat_list = OrderSerializers(many=True)
    class Meta:
        model = Meats
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    meats = MeatSerializers(many=True, read_only=True)
    # meat_with_cost = serializers.SerializerMethodField('meat_cost')
    #  def meat_cost(self, obj):
    #      data = Meats.objects.filter
    #      return 

    
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1

class OrderManySerializers(serializers.ModelSerializer):
    meats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Orders
        fields= '__all__'
        depth=1