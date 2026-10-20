
from ninja import NinjaAPI, Router
from .models import OrderModel
from .auth_api import router as auth_router

api = NinjaAPI()

# Create the orders router
router = Router()

# Register the authentication router
api.add_router("/login/", auth_router)


@router.get("/orders/")
def orders_list(request):
    orders = OrderModel.objects.filter(user=request.user)

    return [
        {
            "id": order.id,
            "product_name": order.product_name,
            "amount": str(order.amount),
            "status": order.status,
            "carrier": order.carrier,
            "tracking_number": order.tracking_number,
            "delivery_address": order.delivery_address,
            "created_at": (
                order.created_at.isoformat()
                if order.created_at
                else None
            ),
        }
        for order in orders
    ]


# Register the orders router

api.add_router("/", router)