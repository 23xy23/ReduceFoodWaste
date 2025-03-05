from django.urls import path
from .views import FoodItemListCreateView, FoodItemDetailView

urlpatterns = [
    path("food-items/", FoodItemListCreateView.as_view(), name="food-item-list"),
    path("food-items/<int:pk>/", FoodItemDetailView.as_view(), name="food-item-detail"),
]
