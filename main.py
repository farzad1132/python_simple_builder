from typing import Any, Callable, List, Tuple

def check_type(func: Callable) -> Callable:
    # TODO: add args support
    def inner(**kwargs: Any) -> None:
        # checking type
        for key, value in kwargs.items():
            if not key in func.__annotations__:
                raise Exception(f"kwarg '{key}' not defined")
            
            type = func.__annotations__[key]
            # TODO: add dictionary support
            if type.__origin__ in (list, tuple):
                if not isinstance(value, type.__origin__):
                    raise Exception(f"parameter '{key}' has wrong value type [must be '{type.__origin__}']")
                
                arg_type = type.__args__[0]
                for item in value:
                    if not isinstance(item, arg_type):
                        raise Exception(f"value '{item}' must be '{arg_type}'")
            
            elif not isinstance(value, type):
                raise Exception(f"parameter '{key}' has wrong value type [must be '{type}']")
            
        func(**kwargs)
    
    return inner

@check_type
def rule(target: List[str], dependencies: str):

    def wrapper(func: Callable):

        def inner():
            # handling dependencies
            func()
        
        return inner
    
    return wrapper