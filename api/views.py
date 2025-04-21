from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Product, Promotion, Size, User
from .serializer import ProductSerializer, PromotionSerializer, SizeSerializer, UserSerializer
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request, token_key):
    token = Token.objects.get(key=token_key)
    user = get_object_or_404(User, username=token.user.username)
    serializer = UserSerializer(user)
    return Response({'token': serializer.data})


@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    return Response(UserSerializer(users, many=True).data)


@api_view(['GET'])
def get_product(request, product_type):
    if product_type == "tous":
        products = Product.objects.all()
    else:
        try:
            products = Product.objects.filter(product_type=product_type)
        except Product.DoesNotExist:
            return Response([], status=status.HTTP_404_NOT_FOUND)

    return Response(ProductSerializer(products, many=True).data)


@api_view(['GET'])
def get_promotion(request, pk):
    try:
        promotion = Promotion.objects.filter(id_product=pk)
    except Promotion.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    return Response(PromotionSerializer(promotion, many=True).data)


@api_view(['GET'])
def get_promotions(request):
    try:
        promotion = Promotion.objects.all()
    except Promotion.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    return Response(PromotionSerializer(promotion, many=True).data)


@api_view(['GET'])
def get_size(request, pk):
    try:
        size = Size.objects.filter(id_product=pk)
    except Size.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    return Response(SizeSerializer(size, many=True).data)


@api_view(['GET'])
def get_sizes(request):
    try:
        size = Size.objects.all()
    except Size.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    return Response(SizeSerializer(size, many=True).data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_promotion(request):
    serializer = PromotionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_size(request):
    serializer = SizeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def promotion_details(request, pk):
    try:
        promotion = Promotion.objects.get(pk=pk)
    except Promotion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromotionSerializer(promotion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PromotionSerializer(promotion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        promotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def size_details(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SizeSerializer(size)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
