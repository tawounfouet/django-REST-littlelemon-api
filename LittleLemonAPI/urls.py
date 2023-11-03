from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    #path('menu-items', views.menu_items),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('manager', views.manager_view),
    path('delivery-crew', views.delevery_crew_view),
]