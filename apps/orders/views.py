# Built-in libraries
# Framework libraries
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
# Other libraries
# Project libraries
from apps.orders.models import Orders
from apps.orders.forms import OrdersForm


class OrdersCreateView(View):
    form_class = OrdersForm
    template_name = 'create_order.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            table_number = form.cleaned_data['table_number']
            items = []
            total_price = 0.0
            for name_price in form.cleaned_data['items'].split(','):
                name, price = name_price.split('-')
                items.append({name.strip(): float(price)})
                total_price += float(price)
            Orders.objects.create(
                table_number=table_number,
                items=items,
                total_price=total_price
            )
            return render(request, 'order_complete.html')
        return HttpResponse('oops')


class OrdersListView(View):
    def get(self, request):
        orders = Orders.objects.all().order_by('created_at')
        return render(request, 'list_orders.html', context={'orders': orders})




