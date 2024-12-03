#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
