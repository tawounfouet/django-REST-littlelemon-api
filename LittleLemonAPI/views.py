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


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response({"message": "Hello, " + request.user.username})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "Only Manager, Should See This"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "You are not authorized to see this"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view()
@permission_classes([IsAuthenticated])
def delevery_crew_view(request):
    # delevery crew and manager can see this
    if request.user.groups.filter(name="Manager").exists() or request.user.groups.filter(name="Delivery Crew").exists():
        return Response({"message": "Only Manager and Delivery Crew, Should See This"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "You are not authorized to see this"}, status=status.HTTP_401_UNAUTHORIZED)







