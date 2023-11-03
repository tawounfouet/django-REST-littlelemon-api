from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('categorie/<int:pk>', views.SingleCategoryView.as_view()),

    #path('menu-items', views.menu_items),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    # Cart
    path('cart', views.CartView.as_view()),

    # Orders
    path('order', views.OrderView.as_view()),
    path('order/<int:pk>', views.SingleOrderView.as_view()),
    path('order-items', views.OrderItemView.as_view()),

    path('api-token-auth/', obtain_auth_token),
    path('manager', views.manager_view),
    path('delivery-crew', views.delevery_crew_view),
]