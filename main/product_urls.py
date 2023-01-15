from django.urls import path
from .product_view import *



urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('search/', searchProducts, name="product-search"),
    path('create/', createProduct, name="product-create"),

    path('<str:pk>/reviews/', createProductReview, name="create-review"),
    path('top/', getTopProducts, name='top-products'),
    path('<int:pk>/', getProduct, name="product"),

    path('update/<int:pk>/', updateProduct, name="product-update"),
    path('delete/<int:pk>/', deleteProduct, name="product-delete"),
    path('get_cat/', get_cat, name="get_cat"),
    path('add_cat/', add_cat, name="add_cat"),
    path('deleteCat/<int:pk>/', deleteCat, name="deleteCat"),
    path('get_sub/', get_sub, name="get_sub"),
    path('addSubcat/', addSubcat, name="addSubcat"),
    path('deleteSubcat/<int:pk>/', deleteSubcat, name="deleteSubcat"),
]