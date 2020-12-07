from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No Keyword Arguments Allowed, Sorry :(')
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    return f'Hi, my name is {name}'

@ensure_no_kwargs
def order(main_dish, side_dish):
    return f'I would like to order {main_dish} alongwith {side_dish}'

print(greet('Colt'))
print(order(main_dish = 'Pizza', side_dish = 'Coke'))