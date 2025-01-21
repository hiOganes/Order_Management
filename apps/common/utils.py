# Built-in libraries
# Framework libraries
# Other libraries
# Project libraries

def set_dict_attr(obj, data):
    'Setting attributes to an obj'
    for key, value in data.items():
        setattr(obj, key, value)
    return obj