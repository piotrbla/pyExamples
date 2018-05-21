import matplotlib.pyplot as plt
import numpy as np


def simple_plot():
    x = np.linspace(0, 5, 10)
    y = x ** 2
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)
    axes.plot(x, y, 'r')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_title('title')
    fig.show()


def additional_axes_inside_figure():
    x = np.linspace(0, 5, 10)
    y = x ** 2
    fig = plt.figure()

    axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

    axes1.plot(x, y, 'r')
    axes1.set_xlabel('x')
    axes1.set_ylabel('y')
    axes1.set_title('title')

    axes2.plot(y, x, 'g')
    axes2.set_xlabel('y')
    axes2.set_ylabel('x')
    axes2.set_title('insert title')
    fig.show()


def subplots():
    x = np.linspace(0, 5, 10)
    y = x ** 2
    fig, axes = plt.subplots(nrows=1, ncols=2)

    for ax in axes:
        ax.plot(x, y, 'r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('title')
    fig.show()


def different_styles():
    x = np.linspace(0, 5, 10)
    xx = np.linspace(-0.75, 1., 100)
    n = np.array([0, 1, 2, 3, 4, 5])

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    axes[0].scatter(xx, xx + 0.25 * np.random.randn(len(xx)))
    axes[0].set_title("scatter")
    axes[1].step(n, n ** 2, lw=2)
    axes[1].set_title("step")
    axes[2].bar(n, n ** 2, align="center", width=0.5, alpha=0.5)
    axes[2].set_title("bar")
    axes[3].fill_between(x, x ** 2, x ** 3, color="green", alpha=0.5)
    axes[3].set_title("fill_between")
    fig.show()


if __name__ == '__main__':
    different_styles()
