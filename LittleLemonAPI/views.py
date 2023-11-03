from django.shortcuts import render


from rest_framework import status, generics
from rest_framework.response import Response
#from rest_framework.decorators import api_view


# Create your views here.
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# @api_view(["GET", "POST"])
# def menu_items(request):
#     # Get Request
#     if request.method == "GET":
#         items = MenuItem.objects.select_related("category").all()
#         serialized_items = MenuItemSerializer(items, many=True)
#         return Response(serialized_items.data)

#     # Post Request
#     elif request.method == "POST":
#         serialized_item = MenuItemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
#         return Response(serialized_item.data, status=status.HTTP_201_CREATED)






