from abc import ABC, abstractmethod

def decorator(cls):
    class BaseClass(cls):
        def __init__(self):
            print('Instantiated a newly created object of the BaseClass')

    return BaseClass

@decorator
class SubClass:
    pass

o = SubClass()