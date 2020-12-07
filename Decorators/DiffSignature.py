def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()

    return wrapper

@shout
def greet(name):
    return f'Hi i am {name}'

@shout
def order(main, side):
    return f'I would like to order {main} alongwith {side}'

@shout
def lol():
    return 'lol'


print(greet('Jason'))
print(order('FarmHouse Pizza', 'Lava Cake'))
print(lol())


