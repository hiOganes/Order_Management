# Built-in libraries
# Framework libraries
from django import forms
# Other libraries
# Project libraries


class OrdersForm(forms.Form):
    table_number = forms.IntegerField(label='Номер столика', min_value=1)
    items = forms.CharField(widget=forms.Textarea(), label='Блюдо')