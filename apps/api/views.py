# Built-in libraries
from http import HTTPStatus
# Framework libraries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# Other libraries
from drf_spectacular.utils import extend_schema, OpenApiParameter
# Project libraries
from apps.orders.models import Orders
from apps.api.serializers import OrdersUpdateSerializer, OrdersCreateSerializer
from apps.common.utils import set_dict_attr


tags = ['Orders']


class ListOrdersAPIView(APIView):
    serializer_class = OrdersCreateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['table_number', 'status']

    @extend_schema(
        summary='This endpoint return list orders',
        tags=['Orders'],
        parameters=[
            OpenApiParameter(
                'table_number',
                int,
                description='Искать по номеру столика',
                required=False
            ),
            OpenApiParameter(
                'status',
                str,
                description='Искать по статусу заказа',
                required=False,
                enum=[status[0] for status in Orders.Status.choices]
            ),
        ]
    )
    def get(self, request):
        table_number = request.query_params.get('table_number', None)
        status = request.query_params.get('status', None)

        if table_number is not None:
            orders = Orders.objects.filter(table_number=table_number)

        if status is not None:
            orders = Orders.objects.filter(status=status)

        if table_number is None and status is None:
            orders = Orders.objects.all()

        serializer = self.serializer_class(orders, many=True)
        return Response(data=serializer.data, status=HTTPStatus.OK)

    @extend_schema(
        summary='This endpoint create order',
        tags=tags
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        total_price = 0
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.validated_data['total_price'] = 0
            for field in serializer.validated_data['items']:
                 serializer.validated_data['total_price'] += field['price']
            new_order = Orders.objects.create(**serializer.validated_data)
            serializer = self.serializer_class(new_order)
            return Response(data=serializer.data, status=HTTPStatus.CREATED)
        return Response(data=serializer.errors, status=HTTPStatus.BAD_REQUEST)


class DetailOrdersAPIView(APIView):
    serializer_class = OrdersUpdateSerializer
    fields = ['status']

    def get_object(self, *args, **kwargs):
        try:
            return Orders.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExists:
            return Response(
                data={'Заказ не найден'},
                status=HTTPStatus.NOT_FOUND
            )

    @extend_schema(
        summary='This endpoint change status order',
        tags=tags,
    )
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        order = self.get_object(pk=kwargs['pk'])
        if serializer.is_valid():
            order = set_dict_attr(order, serializer.validated_data)
            order.save()
            serializer = self.serializer_class(order)
            return Response(data=serializer.data, status=HTTPStatus.OK)
        return Response(data=serializer.errors, status=HTTPStatus.BAD_REQUEST)



    @extend_schema(
        summary='This endpoint delete order',
        tags=tags,
    )
    def delete(self, request, *args, **kwargs):
        order = self.get_object(pk=kwargs['pk'])
        order.delete()
        return Response(data={'Заказ удалён'}, status=HTTPStatus.OK)