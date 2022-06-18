from django.db import models
from rest_framework import serializers
from datetime import datetime
from django_mysql.models import ListCharField

# Create your models here
class Item(models.Model):
    food_category = models.CharField(max_length =15)
    food_title = models.CharField(max_length=20)
    food_type = models.CharField(max_length=15, blank=True, default = '')
    food_size = models.CharField(max_length=15 , default='')
    food_rate = models.IntegerField()
    def __str__(self):
        return self.food_title

class Table(models.Model):
    table_code = models.CharField(max_length=10)
    table_status = models.BooleanField(default=False)
    table_capacity = models.IntegerField()
    table_info = models.TextField(null=True, blank=True, max_length=200)
    def __str__(self):
        return self.table_code

class Staff(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15)
    code  = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return self.first_name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    token = models.CharField(max_length=15)#auto generate
    order_settled = models.BooleanField(default=False)
    no_of_people = models.IntegerField()
    # total_price  = models.FloatField(max._length=15)#from the items selected calculated backend
    def __str__(self):
        return self.token

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=5, null=True, default=0.0)
    served = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    special = models.TextField(max_length = 200,null=True, blank=True)
    def __str__(self):
        return str(self.item_id)

class Vendor(models.Model):
    vendor_title = models.CharField(max_length=25)
    Vendor_mobile = models.CharField(max_length=15)
    def __str__(self):
        return self.vendor_title

class VendorOrder(models.Model):
    vernder_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    token = models.CharField(max_length=15)
    total_price  = models.FloatField(max_length=5)
    discount = models.FloatField(max_length=5, null=True, default=0.0)
    vender_request =models.TextField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.token

class VendorOrderItem(models.Model):
    vender_order_id = models.ForeignKey(VendorOrder, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=5, null=True, default=0.0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    special = models.TextField(max_length = 200,null=True, blank=True)
    def __str__(self):
        return str(self.item_id)

