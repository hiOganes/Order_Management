# Built-in libraries
from http import HTTPStatus
# Framework libraries
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
# Other libraries
# Project libraries
from apps.orders.models import Orders
from apps.api.views import ListOrdersAPIView, DetailOrdersAPIView


class OrdersListTests(TestCase):
    fixtures = ['fixtures/db_orders.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('list-api')
        self.orders = Orders.objects.all()
        self.view = ListOrdersAPIView.as_view()
        self.data = {
            'table_number': 3,
            'items': [{'name': 'Test', 'price': 1}]
        }

    def test_get_orders_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(self.orders), len(response.data))

    def test_create_orders(self):
        count_orders = self.orders.count()
        request = self.factory.post(self.url, self.data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(count_orders + 1, self.orders.count())


class OrdersDetailTests(TestCase):
    fixtures = ['fixtures/db_orders.json']

    def setUp(self):
        self.orders = Orders.objects.all()
        self.pk = self.orders[0].id
        self.url = reverse('detail-orders-api', kwargs={'pk': self.pk})
        self.factory = APIRequestFactory()
        self.view = DetailOrdersAPIView.as_view()

    def test_delete_orders(self):
        count_orders = self.orders.count()
        request = self.factory.delete(self.url)
        response = self.view(request, pk=self.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(count_orders - 1, self.orders.count())

    def test_update_orders(self):
        data = {"status": "Готово"}
        request = self.factory.put(self.url, data=data)
        response = self.view(request, pk=self.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Orders.objects.get(pk=self.pk).status, 'Готово')
