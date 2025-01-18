# Built-in libraries
# Framework libraries
from django import forms
# Other libraries
# Project libraries
from apps.orders.models import Orders


class OrdersForm(forms.ModelForm):
    items = forms.JSONField(label='Меню', initial=[{"name": "", "price": ""}])
    class Meta:
        model = Orders
        fields = ['table_number', 'items', 'status']
        labels = {
            'table_number': 'Номер столика',
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск заказа')