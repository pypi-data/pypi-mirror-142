from typing import Union


def power(x: float, y: int) -> float:
    return x**y


def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x * y


def cast_int(x: Union[int, float]) -> int:
    return int(x)
