
from django.contrib import admin
from .models import ProductModel, OrderModel, RefundRequestModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "inStock")
    search_fields = ("name", "category")
    list_filter = ("category", "inStock")
    ordering = ("name",)


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product_name",
        "amount",
        "status",
        "carrier",
        "tracking_number",
        "created_at",
    )
    search_fields = (
        "product_name",
        "tracking_number",
        "user__username",
    )
    list_filter = ("status", "carrier", "created_at")
    ordering = ("-created_at",)


@admin.register(RefundRequestModel)
class RefundRequestModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "user",
        "status",
        "created_at",
    )
    search_fields = (
        "order__product_name",
        "user__username",
        "reason",
    )
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)
