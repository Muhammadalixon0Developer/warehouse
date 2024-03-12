from rest_framework import serializers
from .models import *


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

    
class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = ['product', 'material', 'quantity']
    

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['material', 'reminder', 'price']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['product', 'product_qty']



