from django.db import models

# Create your models here.
class TablestableInStore(models.Model):
    name = models.CharField(max_length=10)

class  Tabledailydate(models.Model):

    OPEN = 'OPEN'
    CLOSE = 'CLOSE'

    Status_Table = [
        (OPEN, 'OPEN'),
        (CLOSE, 'CLOSE'),
    ]

    status = models.CharField(
                max_length=5,
                choices=Status_Table,
                default=OPEN
            )
    people_count = models.IntegerField()
    table_open_time = models.DateTimeField(auto_created=True)
    table_close_time = models.DateTimeField(null=True,blank=True)

    table = models.ForeignKey(TablestableInStore,on_delete=models.CASCADE,related_name='table_of_dailytable')
    def __str__(self):
        return f' Table Name : {self.table.name}, Status : {self.status}, DT : {self.table_open_time}'

class TypeOfMeat(models.Model):
    name_type = models.CharField(max_length=255)

class Meats(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    type = models.ForeignKey(TypeOfMeat, on_delete=models.CASCADE, related_name='type_of_meat')
    def __str__(self):
        return f'name : {self.name}, quantity : {self.quantity}, type : {self.type.name_type}'

class Orders(models.Model):
    
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

    meats  = models.ManyToManyField(Meats)

    table = models.ForeignKey(Tabledailydate,on_delete=models.CASCADE,related_name='order_table')

    # def __str__(self) -> str:
    #     # meat_list  = ''.join(self.meat)

    #     return f'id :{self.id},  status:{self.status.all()}'


