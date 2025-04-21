from django.urls import path
from .views import create_size, get_size, get_sizes, get_user, create_user, login, product_details, signup, size_details, test_token, user_details, get_product, create_product, get_promotion, get_promotions, create_promotion, promotion_details

urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('test-token/<str:token_key>', test_token, name="test_token"),

    path('user', get_user, name="get_user"),
    path('create-user', create_user, name="create_user"),
    path('user-details/<int:pk>', user_details, name="user_details"),

    path('product/<str:product_type>', get_product, name="get_product"),
    path('create-product', create_product, name="create_product"),
    path('product-details/<int:pk>', product_details, name="product-details"),

    path('promotion', get_promotions, name="get_promotions"),
    path('promotion/<int:pk>', get_promotion, name="get_promotion"),
    path('create-promotion', create_promotion, name="create_promotion"),
    path('promotion-details/<int:pk>', promotion_details, name="promotion-details"),

    path('size', get_sizes, name="get_size"),
    path('size/<int:pk>', get_size, name="get_size"),
    path('create-size', create_size, name="create_size"),
    path('size-details/<int:pk>', size_details, name="size-details")
]
