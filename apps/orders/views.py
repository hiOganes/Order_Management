# Built-in libraries
import json
# Framework libraries
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    UpdateView,
    ListView,
    CreateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector
# Other libraries
# Project libraries
from apps.orders.models import Orders
from apps.orders.forms import OrdersForm, SearchForm


class OrdersCreateView(CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'create_order.html'
    success_url = reverse_lazy('list-orders')

    def form_valid(self, form):
        total_price = 0
        for item in form.cleaned_data['items']:
            item['name'] = item['name'].title()
            item['price'] = float(item['price'])
            total_price += item['price']
        form.instance.total_price = total_price
        return super().form_valid(form)


class OrdersListView(ListView):
    template_name = 'list_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Orders.objects.all()
        if 'query' in self.request.GET:
            form = SearchForm(self.request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']
                orders = Orders.objects.annotate(
                    search=SearchVector('table_number', 'status'),
                ).filter(search=query)
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = SearchForm()
        return context


class OrdersDeleteView(DeleteView):
    model = Orders
    success_url = reverse_lazy('list-orders')


class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = 'update_orders.html'
    success_url = reverse_lazy('list-orders')
    fields = ['status']


class TotalIncome(TemplateView):
    template_name = 'total_income.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Orders.objects.filter(status='Оплачено')
        context['total_income'] = 0
        for order in orders:
            context['total_income'] += order.total_price
        return context





