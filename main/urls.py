from django.urls import path

from .orderview import *
from .views import *
from .product_view import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenBlacklistView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('register/', registerUser, name='register'),

    path('profile/', getUserProfile, name="users-profile"),
    path('profile/update/', updateUserProfile, name="user-profile-update"),
    path('', getUsers, name="users"),

    path('<str:pk>/', getUserById, name='user'),

    path('update/<str:pk>/', updateUser, name='user-update'),

    path('delete/<str:pk>/', deleteUser, name='user-delete'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blogs/<str:pk>/', getBlog, name='blogs'),
    path('blogs/search/', searchBlog, name="blogs-search"),
    path('blogs/create/', createBlog, name="product-blogs"),
    path('blogs/update/<int:pk>/', updateBlog, name="blogs-update"),
    path('blogs/delete/<int:pk>/', deleteBlogs, name="blogs-delete"),
    path('story/', get_story, name='story'),
    # product urls

    path('products/', ProductView.as_view(), name='products'),
    path('products/search/', searchProducts, name="product-search"),
    path('products/create/', createProduct, name="product-create"),

    path('products/<str:pk>/reviews/', createProductReview, name="create-review"),
    path('products/top/', getTopProducts, name='top-products'),
    path('products/<int:pk>/', getProduct, name="product"),

    path('products/update/<int:pk>/', updateProduct, name="product-update"),
    path('products/delete/<int:pk>/', deleteProduct, name="product-delete"),
    path('products/get_cat/', get_cat, name="get_cat"),
    path('products/add_cat/', add_cat, name="add_cat"),
    path('products/deleteCat/<int:pk>/', deleteCat, name="deleteCat"),
 path('products/get_sub/', get_sub, name="get_sub"),
    path('products/addSubcat/', addSubcat, name="addSubcat"),
    path('products/deleteSubcat/<int:pk>/', deleteSubcat, name="deleteSubcat"),

    # order urls

    path('', getOrders, name='orders'),
    path('orders/add/', addOrderItems, name='orders-add'),
    path('orders/myorders/', getMyOrders, name='myorders'),

    path('orders/<int:pk>/deliver/', updateOrderToDelivered, name='order-delivered'),

    path('orders/<int:pk>/', getOrderById, name='user-order'),
    path('orders/<int:pk>/pay/', updateOrderToPaid, name='pay'),







]


