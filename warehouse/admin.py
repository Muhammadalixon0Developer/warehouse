from django.contrib import admin
from .models import *

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['material', 'pk', 'reminder', 'price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ['product', 'material', 'quantity']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_qty']

admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Order, OrderAdmin)

    