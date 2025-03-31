from django.urls import path
from .views import get_user, create_user, user_details, get_product, create_product

urlpatterns = [
    path('user/', get_user, name="get_user"),
    path('user/create', create_user, name="create_user"),
    path('user/<int:pk>', user_details, name="user_details"),
    path('product/<str:product_type>', get_product, name="get_product"),
    path('product/create', create_product, name="create_product")
]
