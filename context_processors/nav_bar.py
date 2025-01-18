nav = [
    {'name': 'Сделать заказ', 'name_url': 'create-orders'},
    {'name': 'Все заказы', 'name_url': 'list-orders'},
    {'name': 'Общая выручка', 'name_url': 'total-income'},
    ]

def get_nav(request):
    return {'mainnav': nav}