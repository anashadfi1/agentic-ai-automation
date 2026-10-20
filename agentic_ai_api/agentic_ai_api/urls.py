from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from orders import urls
from django.urls import include
api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", api.urls),
    path("logout/", api.urls),
    path("register/", api.urls),


]