from random import sample
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering


def test_pandas_series():
    x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
    print(x)
    data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'],
            'age': [29, 31, 27, 35],
            'ZIP': ['02115', '02130', '67700', '00100']}


def get_whiskies_data():
    whisky = pd.read_csv("whiskies.txt")
    whisky["Region"] = pd.read_csv("regions.txt")
    return whisky


def plot_flavors_correlation(flavors):
    # print(flavors.head())
    corr_flavors = pd.DataFrame.corr(flavors)
    # print(corr_flavors)
    plt.figure(figsize=(10, 10))
    plt.pcolor(corr_flavors)
    plt.colorbar()
    plt.show()


def plot_correlations(corr_whiskies):
    plt.figure(figsize=(10, 10))
    plt.pcolor(corr_whiskies)
    plt.axis("tight")
    plt.colorbar()
    plt.show()


def plot_transposed_correlation(flavors):
    corr_whiskies = pd.DataFrame.corr(flavors.transpose())
    # print(corr_whiskies)
    plot_correlations(corr_whiskies)


def cluster_data(flavors, whisky):
    corr_whisky = pd.DataFrame.corr(flavors.transpose())
    model = SpectralCoclustering(n_clusters=6, random_state=0)
    model.fit(corr_whisky)
    whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
    whisky = whisky.ix[np.argsort(model.row_labels_)]
    whisky = whisky.reset_index(drop=True)
    correlation = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
    correlation = np.array(correlation)
    # print(np.sum(model.rows_, axis=1))
    # print(np.sum(model.rows_, axis=0))
    # print(model.row_labels_)
    # print(correlation)
    plot_correlations(correlation)


if __name__ == '__main__':
    whisky_data = get_whiskies_data()
    geo_data = whisky_data.iloc[5:10, 15:17]
    flavors_data = whisky_data.iloc[:, 2:14]
    # plot_flavors_correlation(flavors_data)
    # plot_transposed_correlation(flavors_data)
    # cluster_data(flavors_data, whisky_data)
    data = pd.Series([1, 2, 3, 4])
    print(data)
    data = data.ix[[3, 0, 1, 2]]
    print(data)
    data = data.reset_index(drop=True)
    print(data)
    print(data[0])
