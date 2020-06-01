import random

from typing import Callable, Union

import numpy as np

AMPLITUDE: float = 1
FULL_CIRCLE = 2 * np.pi

HARMONICS: int = 6
FREQUENCY: int = 1700
DISCRETE_COUNTS: range = range(1024)

GeneratorTicker = Callable[[float], float]


def generator(harmonics: int, frequency: int) -> GeneratorTicker:
    A = np.array([random.uniform(-AMPLITUDE, AMPLITUDE) for _ in range(harmonics)])
    phi = np.array([FULL_CIRCLE * random.uniform(-1, 1) for _ in range(harmonics)])
    w = frequency / harmonics

    def tickerFn(t: Union[int, float]) -> float:
        return np.sum(A * np.sin(w * np.arange(harmonics) * t + phi))

    return tickerFn
