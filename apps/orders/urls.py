# Built-in libraries
# Framework libraries
from django.urls import path
# Other libraries
# Project libraries
from apps.orders import views


urlpatterns = [
    path('create-orders/', views.OrdersCreateView.as_view(), name='create-orders'),
    path('list-orders/', views.OrdersListView.as_view(), name='list-orders'),
]