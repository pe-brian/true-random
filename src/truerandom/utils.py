from functools import wraps
from typing import Any


def auto_checks(
    func
):
    """
        Automatically checks the types of parameters passed to a function
        (using the function annotations)
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


def evaluate(
    left: Any,
    right: Any,
    operator: str
):
    """
        Evaluate a simple expression
    """
    if operator == '==':
        return left == right
    if operator == '!=':
        return left != right
    if operator == '>':
        return left > right
    if operator == '<':
        return left < right
    if operator == '>=':
        return left >= right
    if operator == '<=':
        return left <= right
    if operator == 'in':
        return left in right
    if operator == 'not in':
        return left not in right


def check_rule(
    param_name: str,
    operator: str,
    value: Any
):
    """
        Check if the function parameter value
        respects a certain rule
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if param_name in kwargs:
                param_value = kwargs[param_name]
                if not evaluate(param_value, value, operator):
                    raise ValueError(
                        f"{param_name} must be {operator} {param_value} "
                        f"(current: {param_value}).")
            return func(*args, **kwargs)
        return wrapper
    return decorator
