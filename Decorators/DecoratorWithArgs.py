from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                raise ValueError(f'First argument should be {val}')
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is('Umang')
def get_name(first_name, last_name):
    return f'My name is {first_name} {last_name}'

@ensure_first_arg_is('Bruce')
def get_batman(real_name, age):
    return f'Batman\'s real name is {real_name} and age is {str(age)}'

print(get_name('Umang','Bhatia'))
print(get_batman('Jason',30))

