from django.urls import path
from .views import get_user, create_user, product_details, user_details, get_product, create_product

urlpatterns = [
    path('user/', get_user, name="get_user"),
    path('create-user', create_user, name="create_user"),
    path('user-details/<int:pk>', user_details, name="user_details"),

    path('product/<str:product_type>', get_product, name="get_product"),
    path('create-product', create_product, name="create_product"),
    path('product-details/<int:pk>', product_details, name="create_product")
]
