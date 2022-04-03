from django.contrib import admin

from custom.models import Category, Product, Inventory

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
