from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def get_warehouse_data(request):
    order_id = request.GET.get('order_id', None)
    order = get_object_or_404(Order, id=order_id) if order_id else None

    if order:
        warehouse_data = []
        product_name = order.product.name
        product_qty = order.product_qty
        product_materials_qty = []

        for product_material in ProductMaterial.objects.filter(product__name=product_name):
            product_material_qty = product_material.quantity * product_qty
            warehouse = Warehouse.objects.filter(material=product_material.material).first()
            total_price = warehouse.price * product_qty


            if warehouse:
                product_materials_qty.append({
                    'material_name': product_material.material.name,
                    'qty': product_material_qty,
                    'price': warehouse.price,
                    'total_price': total_price
                })

        warehouse_data.append({
            'product': product_name,
            'product_qty': product_qty,
            'product_materials': product_materials_qty
        })

        return JsonResponse({'result': warehouse_data})
    else:
        return JsonResponse({'error': 'Order not found'})

