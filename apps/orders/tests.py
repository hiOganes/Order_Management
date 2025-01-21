from http import HTTPStatus
from django.urls import reverse
from django.test import TestCase
from .models import Orders

class OrdersViewTests(TestCase):
    fixtures = ['fixtures/db_orders.json']

    def setUp(self):
        self.data = {
            'table_number': 1,
            'items': [{"name": "Test", "price": "100"}]
        }
        self.orders = Orders.objects.all()
        self.status = 'Готово'

    def test_orders_list(self):
        path = reverse('list-orders')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_orders_delete(self):
        path = reverse('delete-orders', kwargs={'pk':self.orders[0].id})
        response = self.client.delete(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_orders_update(self):
        path = reverse('update-orders', kwargs={'pk':self.orders[0].id})
        response = self.client.post(path, data={'status': self.status})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_total_income(self):
        path = reverse('total-income')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def tearDown(self):
        pass
