from functools import wraps


def check_params(func):
    """
        Automatically checks the types of parameters passed to a function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for param_name, param_type in func.__annotations__.items():
            if param_name in kwargs:
                param_value = kwargs[param_name]
                if not isinstance(param_value, param_type):
                    raise TypeError(
                        f"Param '{param_name}' must be of type '"
                        f"{param_type.__name__}'")
        return func(*args, **kwargs)
    return wrapper
