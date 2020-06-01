if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    from signal_11 import *

    from . import autocorr

    x_gen = generator(HARMONICS, FREQUENCY)
    y_gen = generator(HARMONICS, FREQUENCY)

    sig_x = np.array([x_gen(lag) for lag in DISCRETE_COUNTS])
    sig_y = np.array([y_gen(lag) for lag in DISCRETE_COUNTS])

    Rxx = autocorr(sig_x, sig_x)
    Rxy = autocorr(sig_x, sig_y)

    fig, axs = plt.subplots(3, 1)

    axs[0].plot(DISCRETE_COUNTS, Rxx)
    axs[0].set_xlabel('Lags')
    axs[0].set_ylabel('Rxx(t, lag)')

    axs[1].plot(DISCRETE_COUNTS, Rxy)
    axs[1].set_xlabel('Lags')
    axs[1].set_ylabel('Rxy(t, lag)')

    axs[2].plot(DISCRETE_COUNTS, Rxx, DISCRETE_COUNTS, Rxy)
    axs[2].set_xlabel('Lags')
    axs[2].set_ylabel('Rxx, Rxy')

    fig.tight_layout()
    plt.show()
