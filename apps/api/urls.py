# Built-in libraries
# Framework libraries
# Other libraries
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
# Project libraries
from apps.api import views


urlpatterns = [
    path('list/', views.ListOrdersAPIView.as_view(), name='list-api'),
    path('detail/<uuid:pk>/', views.DetailOrdersAPIView.as_view(), name='detail-orders-api'),
    # Download schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # API Doc:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]