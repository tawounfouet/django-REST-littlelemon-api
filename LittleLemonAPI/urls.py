from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    #path('menu-items', views.menu_items),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    path('manager', views.manager_view),
    path('delivery-crew', views.delevery_crew_view),
]