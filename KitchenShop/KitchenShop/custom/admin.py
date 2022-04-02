from django.contrib import admin

from custom.models import Product, Inventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
