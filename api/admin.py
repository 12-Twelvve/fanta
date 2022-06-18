from django.contrib import admin
from api.models import Item, Table, Order, OrderItem, Staff, Vendor, VendorOrder, VendorOrderItem
# Register your models here.

admin.site.register(Item)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(VendorOrder)
admin.site.register(VendorOrderItem)
