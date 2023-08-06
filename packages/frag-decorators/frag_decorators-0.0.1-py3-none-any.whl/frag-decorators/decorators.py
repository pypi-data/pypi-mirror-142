from functools import wraps
import typing
import inspect
import time
from functools import wraps


def output_time(func):
    """
    函数用时
    """
    @wraps(func)
    def inner(*args, **kwargs):
        s = time.time()
        rst = func(*args, **kwargs)
        e = time.time()
        print(f'函数 {inner.__name__} 运行时长为 {round(e-s, 4)}s')
        return rst
    return inner


def check_type(func):
    """
    函数类型检查
    """
    type_map = typing.get_type_hints(func)
    sign = inspect.signature(func)

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal type_map
        bind = sign._bind(args, kwargs)
        for param_name, param_value in bind.arguments.items():
            if param_name in type_map and not isinstance(param_value, type_map[param_name]):
                raise Exception("参数类型有误")
        return func(*args, **kwargs)
    return inner
