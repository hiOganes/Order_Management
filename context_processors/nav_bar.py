nav = [
    {'name': 'Order', 'name_url': 'create-orders'},
    {'name': 'All', 'name_url': 'list-orders'},
    # {'name': 'Search', 'name_url': 'search'}
    ]

def get_nav(request):
    return {'mainnav': nav}