if __name__ == '__main__':
    import numpy as np

    from . import generator, AMPLITUDE, DISCRETE_COUNTS, FREQUENCY, HARMONICS


    x_gen = generator(HARMONICS, FREQUENCY)

    sig_x = np.array([x_gen(lag) for lag in DISCRETE_COUNTS])

    import matplotlib.pyplot as plt
    plt.plot(DISCRETE_COUNTS, sig_x, label='x')
    plt.title('Random signals')
    plt.legend()
    plt.show()
