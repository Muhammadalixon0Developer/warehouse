from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
from .views import get_warehouse_data

router = SimpleRouter()
router.register('productmaterial', ProductMaterialViewSet, basename='productmaterial')
router.register('product', ProductViewSet, basename='product')
router.register('order', OrderViewSet, basename='order')
router.register('material', MaterialViewSet, basename='material')
router.register('warehouse', WarehouseViewSet, basename='warehouse')

app_name = 'warehouse'
urlpatterns = [
    path('', include(router.urls)),
    path('get_warehouse_data/', get_warehouse_data, name='get_warehouse_data')
]

