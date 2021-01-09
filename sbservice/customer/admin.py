from django.contrib import admin
from customer.models import TablestableInStore , Tabledailydate , Meats , Orders, TypeOfMeat
# Register your models here.
admin.site.register(TablestableInStore)
admin.site.register(Tabledailydate)
admin.site.register(Meats)
admin.site.register(Orders)
admin.site.register(TypeOfMeat)