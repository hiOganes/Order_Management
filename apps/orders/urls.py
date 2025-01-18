# Built-in libraries
# Framework libraries
from django.urls import path
# Other libraries
# Project libraries
from apps.orders import views


urlpatterns = [
    path(
        'create/',
        views.OrdersCreateView.as_view(),
        name='create-orders'
    ),
    path(
        'list/',
        views.OrdersListView.as_view(),
        name='list-orders'
    ),
    path(
        'delete/<uuid:pk>/',
        views.OrdersDeleteView.as_view(),
        name='delete-orders'
    ),
    path(
        'update/<uuid:pk>/',
        views.OrdersUpdateView.as_view(),
        name='update-orders'
    ),
]