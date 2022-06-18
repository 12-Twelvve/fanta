from rest_framework import serializers
from api.models import Item, Table, Order, OrderItem, Staff, Vendor, VendorOrder, VendorOrderItem
from drf_writable_nested import WritableNestedModelSerializer

class ItemSerializer( serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # table_id = TableSerializer()
    # staff_id = StaffSerializer()
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['created_at', 'table_id', 'staff_id', 'token','no_of_people']
    
class OrderItemSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # order_id = OrderSerializer()
    # item_id = ItemSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'
    
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
    
class VendorOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorOrder
        fields = '__all__'
    
class VendorOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorOrderItem
        fields = '__all__'
    

