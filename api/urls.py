from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
 
router = DefaultRouter()
router = DefaultRouter()

router.register('item', views.ItemView, basename ='item')
router.register('table', views.TableView, basename ='table')
router.register('staff', views.StaffView, basename ='staff')
router.register('order', views.OrderView, basename ='order')
router.register('orderitem', views.OrderItemView, basename ='orderitem')
# router.register('vendor', views.OrderView, basename ='vendororder')
# router.register('vendoritem', views.OrderView, basename ='vendorordoritem')


urlpatterns = [
    path('', include(router.urls)),
]