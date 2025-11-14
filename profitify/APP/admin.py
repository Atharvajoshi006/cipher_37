from django.contrib import admin
from . import models

# Register your models here so you can see them in the /admin/ panel

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'barcode', 'selling_price', 'cost_price')
    search_fields = ('product_name', 'barcode')

@admin.register(models.StockBatch)
class StockBatchAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'received_date', 'expiry_date')
    list_filter = ('expiry_date', 'received_date')

@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_timestamp', 'total_amount', 'total_profit', 'user')
    list_filter = ('sale_timestamp', 'user')

@admin.register(models.SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'price_at_sale')

@admin.register(models.Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'product', 'message', 'created_at', 'is_viewed')
    list_filter = ('alert_type', 'is_viewed')

@admin.register(models.PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status',)

@admin.register(models.PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'product', 'quantity')