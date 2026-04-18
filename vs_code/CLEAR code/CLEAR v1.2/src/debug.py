import utime  # type: ignore


"""Used for debugging functions in code."""

@staticmethod
def start(func):
    """Does error handling, prints all variables, and gives time fof funtion."""

    def wrapper(*args, **kwargs):
        try:
            speed:float=utime.ticks_ms()
            print("Startingdebug for %s"%(func))
            func(*args, **kwargs)
            print(func)
            print("Time of function: %f Msec"%((utime.ticks_diff(utime.ticks_ms, speed))))
            print(locals())
        except Exception as e:
            sys.print_exception(e) # type: ignore
    return wrapper

@staticmethod
def handling(func):
    """Puts in error handling."""

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            sys.print_exception(e) # type: ignore
    return wrapper

@staticmethod
def print(func):
    """Prints variables."""

    def wrapper(*args, **kwargs):
        print("Startingdebug for %s"%(func))
        func(*args, **kwargs)
        print(func)
        print(locals())
    return wrapper

@staticmethod
def time(func):
    """Prints time to exec the function."""

    def wrapper(*args, **kwargs):
        speed:float=utime.ticks_ms()
        func(*args, **kwargs)
        print("Time of function: %f Msec"%((utime.ticks_diff(utime.ticks_ms(), speed))))
    return wrapper