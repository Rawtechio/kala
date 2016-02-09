import random


in_percentage = lambda x: random.randint(1, 100) <= x


def sometimes(fn):
    """
    They've done studies, you know. 50% of the time,
    it works every time.
    """

    def wrapped(*args, **kwargs):
        wrapped.x += 1
        if wrapped.x % 2 == 1:
            return fn(*args, **kwargs)

    wrapped.x = 0
    return wrapped

half_the_time = sometimes


def sometimesish(fn):
    """
    Has a 50/50 chance of calling a function
    """
    def wrapped(*args, **kwargs):
        if random.randint(1, 2) == 1:
            return fn(*args, **kwargs)

    return wrapped


def percent_of_the_time(p):
    """
    Function has a X percentage chance of running
    """
    def decorator(fn):

        def wrapped(*args, **kwargs):
            if in_percentage(p):
                fn(*args, **kwargs)

        return wrapped

    return decorator


def rarely(fn):
    """
    Only 5% chance of happening
    """
    def wrapped(*args, **kwargs):
        if in_percentage(5):
            fn(*args, **kwargs)
    return wrapped


def mostly(fn):
    """
    95% chance of happening
    """
    def wrapped(*args, **kwargs):
        if in_percentage(95):
            fn(*args, **kwargs)
    return wrapped


def times(x, y):
    """
    Do something a random amount of times
    between x & y
    """
    def decorator(fn):

        def wrapped(*args, **kwargs):
            n = random.randint(x, y)
            for z in range(1, n):
                fn(*args, **kwargs)

        return wrapped

    return decorator
