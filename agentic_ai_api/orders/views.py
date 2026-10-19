from django.shortcuts import render
from . import views
from .models import OrderModel

def orders_list(request):
    orders = OrderModel.objects.filter(user=request.user)
    context = {
        'orders' : orders
    }
    return render(request, 'template.html')