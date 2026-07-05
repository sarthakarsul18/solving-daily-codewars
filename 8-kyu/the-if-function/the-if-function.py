from collections.abc import Callable
​
def _if(bool, func1: Callable, func2: Callable):
    return func1() if bool else func2()