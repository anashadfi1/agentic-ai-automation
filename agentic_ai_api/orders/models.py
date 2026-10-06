from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    inStock = models.BooleanField(default=True)

    def __str__(self):
        return self.name






class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('dispatche','Dispatche'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="orders")
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="pending")
    carrier = models.CharField(max_length=100, blank=100)
    tracking_number = models.CharField(max_length=100, blank=True)
    delivery_address = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product_name} - ({self.status})"



class RefundRequestModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('delivered', 'Delivered'),
    ]
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='refund_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refund_requests')
    reason = models.TextField()
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    create_at = models.DateTimeField()
    def __str__(self):
        return f"refund for this order #{self.order.id} - {self.status}"


