from django.urls import path
from .orderview import *




urlpatterns = [
    path('', getOrders, name='orders'),
    path('add/', addOrderItems, name='orders-add'),
    path('myorders/', getMyOrders, name='myorders'),

    path('<int:pk>/deliver/', updateOrderToDelivered, name='order-delivered'),

    path('<int:pk>/', getOrderById, name='user-order'),
    path('<int:pk>/pay/', updateOrderToPaid, name='pay'),
]


