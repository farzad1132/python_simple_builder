from typing import Any, Callable, List

def check_type(func: Callable) -> Callable:
    # TODO: add args support
    def inner(**kwargs: Any) -> None:
        # checking type
        for key, value in kwargs.items():
            if not key in func.__annotations__:
                raise Exception(f"kwarg '{key}' not defined")
            
            if not isinstance(value, func.__annotations__[key]):
                raise Exception(f"parameter '{key}' has wrong value type [must be '{func.__annotations__[key]}']")
            
        func(**kwargs)
    
    return inner

def rule(target: List, *dependencies: str):

    def wrapper(func: Callable):

        def inner():
            # handling dependencies
            func()
        
        return inner
    
    return wrapper