from django.db import models
from rest_framework import serializers
from django.core.serializers import serialize

from .models import tablestableinstore , tabeldailydate , meat , order


class TableDailySerializers(serializers.ModelSerializer):
    class Meta :
        model = tabeldailydate
        fields = '__all__'

class MeatSerializers(serializers.ModelSerializer):
    # meat_list = OrderSerializers(many=True)
    class Meta:
        model = meat
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    meats = MeatSerializers(many=True)
    class Meta:
        model = order
        fields = '__all__'
        depth = 1
