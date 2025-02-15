def decorator(cls):
    return type('', (cls,), {
        'method': lambda self:
            print('A method implementation')
    })

@decorator
class BaseClass:
    pass

o = BaseClass()
o.method()