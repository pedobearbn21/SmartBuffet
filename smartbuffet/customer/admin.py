from django.contrib import admin
from .models import tablestableinstore , tabeldailydate , meat , order
# Register your models here.
admin.site.register(tablestableinstore)
admin.site.register(tabeldailydate)
admin.site.register(meat)
admin.site.register(order)