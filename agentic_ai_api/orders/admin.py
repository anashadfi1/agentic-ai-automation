from django.contrib import admin
from .models import ProductModel, OrderModel, RefundRequestModel
# Register your models here.

class ProductModelAdmin (admin.ModelAdmin):
    list_display = ['name','price','category','inStock']

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user','product_name','amount','status','carrier','tracking_number']

class RefundRequestModelAdmin(admin.ModelAdmin):
    list_display = ['order','user','reason','status','created_at']

admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(RefundRequestModel)