import random
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


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
    return random.choice(winners)


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


def nnk_test_excercise9():
    import pandas as pd
    data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")
    numeric_data = data.drop("color", 1)
    numeric_data = (numeric_data - np.mean(numeric_data, axis=0)) / np.std(numeric_data, axis=0)
    predictors = np.array(numeric_data)

    n_rows = data.shape[0]
    random.seed(123)
    selection = random.sample(range(n_rows), 10)

    training_indices = [i for i in range(len(predictors)) if i not in selection]
    outcomes = np.array(data["high_quality"])
    predictions = [knn_predict(predictors[index], predictors, outcomes, k=5) for index in selection]
    my_predictions = np.array(predictions)
    high_quality = [data.high_quality[x] for x in selection]
    percentage = accuracy(high_quality, my_predictions)
    print(percentage)


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


def plot_prediction_grid(xx, yy, prediction_grid, filename, predictors, outcomes):
    """ Plot KNN predictions for every point on the grid."""
    background_colormap = ListedColormap(["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(10, 10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap=background_colormap, alpha=0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1], c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1');
    plt.ylabel('Variable 2')
    plt.xticks(());
    plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))
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


def sk_test():
    iris = datasets.load_iris()
    predictors = iris.data[:, 0:2]
    outcomes = iris.target
    # plt.plot(predictors[outcomes == 0][:, 0], predictors[outcomes == 0][:, 1], "ro")
    # plt.plot(predictors[outcomes == 1][:, 0], predictors[outcomes == 1][:, 1], "go")
    # plt.plot(predictors[outcomes == 2][:, 0], predictors[outcomes == 2][:, 1], "bo")
    # plt.show()
    k = 5
    file_name = "knn_synth5.pdf"
    limits = (4, 8, 1.5, 4.5)
    h = 0.1
    xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
    # plot_prediction_grid(xx, yy, prediction_grid, file_name, predictors, outcomes)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(predictors, outcomes)
    sk_predictions = knn.predict(predictors)
    my_prediction = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
    print(100 * np.mean(my_prediction == sk_predictions))
    print(100 * np.mean(outcomes == sk_predictions))
    print(100 * np.mean(my_prediction == outcomes))


def exercise_test():
    import pandas as pd
    data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")
    numeric_data = data.drop("color", 1)
    # print(numeric_data[-3:])
    import sklearn.decomposition
    # numeric_data = numeric_data.subtract(np.mean(numeric_data))
    # numeric_data = numeric_data.divide(np.average(numeric_data))
    numeric_data = (numeric_data - np.mean(numeric_data, axis=0)) / np.std(numeric_data, axis=0)

    import sklearn.decomposition
    pca = sklearn.decomposition.PCA(2)
    principal_components = pca.fit(numeric_data).transform(numeric_data)
    print(principal_components)
    n_rows = data.shape[0]

    random.seed(123)
    selection = random.sample(range(n_rows), 10)
    print(selection)

    # print(principal_components[:, 0])
    # print(principal_components[:, 1])


def accuracy(predictions, outcomes):
    same = 100 * np.mean(predictions == outcomes)
    return same


def accuracy_test():
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 4])
    print(accuracy(x, y))


if __name__ == '__main__':
    # accuracy_test()
    # exercise_test()
    nnk_test_excercise9()
    # sk_test()
    # prediction_test()
    # nnk_test()
    # generate_test()
    # test_vote()
    # x = np.random.triangular(5, 10, 20, 11)
    # print(x)
