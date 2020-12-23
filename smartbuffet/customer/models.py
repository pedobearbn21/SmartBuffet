from django.db import models
from django.db.models.aggregates import Count

# Create your models here.
class tablestableinstore(models.Model):
    name = models.CharField(max_length=10)

class  tabeldailydate(models.Model):

    OPEN = 'OPEN'
    CLOSE = 'CLOSE'

    Status_Table = [
        (OPEN, 'open'),
        (CLOSE, 'close'),
    ]

    status = models.CharField(
                max_length=5,
                choices=Status_Table,
                default=OPEN
            )
    people_count = models.IntegerField()
    table_open_time = models.DateTimeField(auto_created=True)
    table_close_time = models.DateTimeField(null=True,blank=True)

    table = models.ForeignKey(tablestableinstore,on_delete=models.CASCADE,related_name='table_of_dailytable')

class meat(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

class order(models.Model):

    ORDERED = 'ORDERED'
    SERVED = 'SERVED'

    Status_Table = [
        (ORDERED, 'ORDERED'),
        (SERVED, 'SERVED'),
    ]

    status = models.CharField(
                max_length=7,
                choices=Status_Table,
                default=ORDERED
            )

    order_time = models.DateTimeField(auto_created=True)
    serve_time = models.DateTimeField(null=True,blank=True)

    meats  = models.ManyToManyField(meat)

    table = models.ForeignKey(tabeldailydate,on_delete=models.CASCADE,related_name='order_table')

    # def __str__(self) -> str:
    #     # meat_list  = ''.join(self.meat)

    #     return f'id :{self.id},  status:{self.status.all()}'

