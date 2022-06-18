from django.shortcuts import render
from api.models import Order, OrderItem, Table, Item, Staff
from api.serializers import OrderSerializer, OrderItemSerializer, TableSerializer, ItemSerializer, StaffSerializer
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend


class TableView(viewsets.ModelViewSet) :
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class StaffView(viewsets.ModelViewSet) :
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ItemView(viewsets.ModelViewSet) :
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderView(viewsets.ModelViewSet) :
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_settled']

class OrderItemView(viewsets.ModelViewSet) :
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['served','order_id']




# @csrf_exempt
# def orderitem(request):
#     if request.method == 'GET':
#         orderItems = OrderItem.objects.all()
#         serializer = OrderItemSerializer(orderItems, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         # print(request)

#         data = JSONParser().parse(request)
#         serializer = OrderItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def orderitem_by_uuid(request, o_i_id):
#     if request.method == 'GET':
#         orderitems = OrderItem.objects.filter(id=o_i_id)
#         serializer = OrderItemSerializer(orderitems, many=False)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = OrderItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'PUT':
#         orderitem = OrderItem.objects.get(id=o_i_id)
#         data = JSONParser().parse(request)
#         serializer = OrderItemSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# {
# "food_category":"momo",
# "food_title":"jhol momo",
# "food_type":"chiken",
# "food_size":"half",
# "food_rate":120,
# "table_code":"12",
# "table_status":True,
# "table_capcity":10,
# "table_info":"corner table",
# "first_name":"biry",
# "last_name":"nepali",
# "code":"S12",
# "mobile":"9876456798",
# "token":"ghklasi243",
# "no_of_people":6,
# "food_category":"pizza",
# "food_title":"red hot pizza",
# "food_size":"21inch",
# "food_rate":1800
# }