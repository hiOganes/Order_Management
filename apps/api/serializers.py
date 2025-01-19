# Built-in libraries
# Framework libraries
from rest_framework import serializers
# Other libraries
# Project libraries
from apps.orders.models import Orders


class OrderItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()

class OrdersCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    total_price = serializers.FloatField(read_only=True)
    status = serializers.CharField(read_only=True)
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Orders
        fields = ['id', 'table_number', 'items', 'total_price', 'status']


class OrdersUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(Orders.Status.choices)
    class Meta:
        model = Orders
        fields = ['status']