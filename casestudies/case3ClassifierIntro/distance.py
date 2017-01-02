from random import choice
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return choice(winners)


def test_distance():
    p1 = np.array([1, 1])
    p2 = np.array([4, 4])
    x = distance(p1, p2)
    print(x)


def test_vote():
    votes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 3, 2, 2, 2]
    winner = majority_vote(votes)
    # print(winner)
    mode, count = ss.mstats.mode(votes)
    # print(mode)


def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    indexes = np.argsort(distances)
    return indexes[:5]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])
    """find and predict the class of p based on majority vote"""


def nnk_test():
    points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
    p = np.array([2.5, 2])
    ind = find_nearest_neighbors(p, points, 2)
    outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
    print(knn_predict(np.array([1.5, 1.7]), points, outcomes, k=2))
    # print(points[ind])

    # print(points[:0], points[:1])
    # print(points[:0], points[:1])
    # # plt.plot(p[0], p[1], "bo")
    # plt.plot(points[:0], points[:1], "ro")
    # plt.axis([0.5, 3.5, 0.5, 3.5])


def generate_synth_data(n=50):
    x = ss.norm(0, 1).rvs((n, 2))
    y = ss.norm(0, 1).rvs((n, 2))
    points = np.concatenate((x, y), axis=0)
    print(x)
    print("break")
    print(y)
    print("break")
    print(points)
    print("break")
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return points, outcomes


def make_prediction_grid(predictors, outcomes, limits, h, k):
    x_min, x_max, y_min, y_max = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return xx, yy, prediction_grid


def generate_test():
    n = 2
    points, outcomes = generate_synth_data(n)
    plt.figure()
    plt.plot(points[:n, 0], points[:n, 1], "ro")
    plt.plot(points[n:, 0], points[n:, 1], "bo")
    plt.savefig("bivariatdata.pdf")

def plot_prediction_grid (xx, yy, prediction_grid, filename, predictors, outcomes):
    """ Plot KNN predictions for every point on the grid."""
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    # plt.savefig(filename)
    plt.show()

def prediction_test():
    predictors, outcomes = generate_synth_data()
    k = 5
    file_name = "knn_synth5.pdf"
    limits = (-3, 4, -3, 4)
    h = 0.1
    xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
    plot_prediction_grid(xx, yy, prediction_grid, file_name, predictors, outcomes)



if __name__ == '__main__':
    prediction_test()
    # nnk_test()
    # generate_test()
    # test_vote()
    # x = np.random.triangular(5, 10, 20, 11)
    # print(x)
