from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(OrderList)
admin.site.register(OrderedItems)