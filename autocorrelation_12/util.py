import numpy as np


def autocorr(x: np.ndarray, y: np.ndarray, mode: str = 'regular') -> np.ndarray:
    """The autocorrelation produces a symmetric signal,
     we only care about the "right half"""
    corr = np.correlate(x, y, mode='full')[len(x) - 1:]
    if mode == 'regular':
        return corr
    elif mode == 'normalized':
        if all(x == y):
            return corr / np.var(x) / len(x)
        else:
            raise ValueError('Different signals')
    else:
        raise ValueError(f'Unknown mode: {mode}')
