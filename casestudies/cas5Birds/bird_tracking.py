import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import networkx as nx

# import cartopy as ctp


def test_birds_tudes():
    bird_data = pd.read_csv("bird_tracking.csv")
    # bird_data.info()
    plt.figure(figsize=(7, 7))
    bird_names = pd.unique(bird_data.bird_name)
    for bird_name in bird_names:
        ix = bird_data.bird_name == bird_name
        x, y = bird_data.longitude[ix], bird_data.latitude[ix]
        plt.plot(x, y, ".", label=bird_name)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(loc="lower right")
    plt.savefig("3traj.pdf")
    plt.show()


def test_birds_speed():
    bird_data = pd.read_csv("bird_tracking.csv")
    # bird_data.info()
    plt.figure(figsize=(7, 7))
    bird_names = pd.unique(bird_data.bird_name)
    for bird_name in bird_names:
        ix = bird_data.bird_name == bird_name
        speed = bird_data.speed_2d[ix]
        ind = ~np.isnan(speed)
        plt.hist(speed[ind], bins=np.linspace(0, 30, 20), normed=True)
        # print(np.isnan(speed).any())
        # print(np.sum(np.isnan(speed)))
    plt.xlabel("2D speed (m/s)")
    plt.ylabel("Frequency")
    # plt.legend(loc="lower right")
    # plt.savefig("speed.pdf")
    plt.show()


def test_birds_speed_pandas():
    bird_data = pd.read_csv("bird_tracking.csv")
    # bird_data.info()
    plt.figure(figsize=(7, 7))
    bird_data.speed_2d.plot(kind='hist', range=[0, 30]) # don't have to deal with NaNs
    plt.xlabel("2D speed (m/s)")
    plt.ylabel("Frequency")
    # plt.legend(loc="lower right")
    # plt.savefig("speed.pdf")
    plt.show()

def add_timestamp(bird_data):
    timestamps = []
    for k in range(len(bird_data)):
        timestamps.append(datetime.datetime.strptime(bird_data.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
    bird_data["timestamp"] = pd.Series(timestamps, index = bird_data.index)



def test_birds_speed_datetime():
    bird_data = pd.read_csv("bird_tracking.csv")
    add_timestamp(bird_data)
    # print(bird_data.timestamp[4] - bird_data.timestamp[3])
    times = bird_data.timestamp[bird_data.bird_name == "Eric"]
    elapsed_time = [time - times[0] for time in times]
    # print(elapsed_time[1000]/datetime.timedelta(hours=1))
    plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
    plt.xlabel("Observation")
    plt.ylabel("Elapsed time (days)")
    plt.show()

def test_birds_speed_mean():
    bird_data = pd.read_csv("bird_tracking.csv")
    add_timestamp(bird_data)
    data = bird_data[bird_data.bird_name == "Eric"]
    times = data.timestamp
    elapsed_time = [time - times[0] for time in times]
    elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
    next_day = 1
    inds = []
    daily_mean_speed = []
    for (i, t) in enumerate(elapsed_days):
        if t<next_day:
            inds.append(i)
        else:
            daily_mean_speed.append(np.mean(data.speed_2d[inds]))
            next_day += 1
            inds = []
    plt.figure(figsize=(8, 6))
    plt.plot(daily_mean_speed)
    plt.xlabel("Day")
    plt.ylabel("Mean speed (m/s)")
    plt.show()

def test_birds_sanne():
    bird_data = pd.read_csv("bird_tracking.csv")
    add_timestamp(bird_data)
    data = bird_data[bird_data.bird_name == "Sanne"]
    print(data[:3])

def test_birds_speed_plot():
    birddata = pd.read_csv("bird_tracking.csv")
    add_timestamp(birddata)
    eric_daily_speed  = birddata.where( birddata.bird_name =="Eric").groupby("altitude").speed_2d.mean()
    # sanne_daily_speed = birddata.where( birddata.bird_name =="Sanne").groupby("date_time").speed_2d
    # nico_daily_speed  = birddata.where( birddata.bird_name =="Nico").groupby("date_time").speed_2d
    eric_daily_speed.plot(label="Eric")
    # sanne_daily_speed.plot(label="Sanne")
    # nico_daily_speed.plot(label="Nico")
    plt.legend(loc="upper left")
    plt.show()


def test_graphs_networks():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_nodes_from(["u", "v"])
    G.add_edge(1, 2)
    G.add_edge("u", "v")
    G.add_edges_from([(1, 3), (1, 4), (1, 5), (1, 6)])
    G.add_edge("u", "w")
    G.remove_node(2)
    G.remove_nodes_from([4, 5])
    G.remove_edge(1, 3)
    G.remove_edges_from([(1, 2), ("u", "v")])
    print(G.nodes())
    print(G.edges())
    print(G.number_of_edges())
    print(G.number_of_nodes())


def test_graphs_karate():
    G = nx.karate_club_graph()
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="grey")
    plt.show()
    # plt.savefig("karate.pdf")
    print(G.number_of_edges())
    print(G.number_of_nodes())
    print(G.degree(0) is G.degree()[0])


def test_bernoulli():
    from scipy.stats import bernoulli
    for i in range(10):
        print(bernoulli.rvs(p=0.1))

def test_erdos_renyi():
    N = 20
    p = 0.2
    G = er_graph(N, p)# print(G.nodes())
    # print(G.edges())
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="grey")
    plt.show()


def er_graph(N, p):
    from scipy.stats import bernoulli
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

def test_graph_degree():
    # D = {1: 1, 2: 2, 3: 3}
    # plt.hist(D) # error
    G1 = er_graph(100, 0.03)
    plot_degree_distribution(G1)
    G2 = er_graph(100, 0.30)
    plot_degree_distribution(G2)
    # G3 = er_graph(500, 0.08)
    # plot_degree_distribution(G3)
    plt.show()

def basic_net_stats(G):
    print("Number of nodes: ", G.number_of_nodes())
    print("Number of edges: ", G.number_of_edges())
    print("Average degree: %.2f" % np.mean(list(G.degree().values())))


def test_graph_india():
    A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
    A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
    G1 = nx.to_networkx_graph(A1)
    G2 = nx.to_networkx_graph(A2)
    basic_net_stats(G1)
    basic_net_stats(G2)
    plot_degree_distribution(G1)
    plot_degree_distribution(G2)
    plt.show()


def test_graph_generator():
    A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
    A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
    G1 = nx.to_networkx_graph(A1)
    G2 = nx.to_networkx_graph(A2)
    gen1 = nx.connected_component_subgraphs(G1)
    G1_LCC = max(gen1, key=len)
    print(len(G1_LCC))
    print(G1.number_of_nodes())
    print(G1_LCC.number_of_nodes())
    print(G1_LCC.number_of_nodes()/G1.number_of_nodes())
    # g1 = gen1.__next__()
    # print(g1)
    # basic_net_stats(G1)
    # basic_net_stats(g1)
    gen2 = nx.connected_component_subgraphs(G2)
    G2_LCC = max(gen2, key=len)
    print(len(G2_LCC))
    print(G2.number_of_nodes())
    print(G2_LCC.number_of_nodes())
    print(G2_LCC.number_of_nodes()/G2.number_of_nodes())
    plt.figure()
    nx.draw(G2_LCC, with_labels=False)
    plt.show()
    # make dict from two panddas columns:
    # pd.Series(df.A.values, index=df.B).to_dict()
    # g2 = gen2.__next__()
    # print(g2)
    # basic_net_stats(G2)
    # basic_net_stats(g2)

def make_dict_from_two_columns():
    df1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
    df2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
    # print(df1.head())
    # sex1 = df1.set_index('icol')['resp_gend'].to_dict()
    sex1 = pd.Series(df1.resp_gend, index=df1.pid).to_dict()

    sex1 = dict(zip(df1.pid, df1.resp_gend))
    caste1 = dict(zip(df1.pid, df1.caste))
    religion1 = dict(zip(df1.pid, df1.religion))
    sex2 = dict(zip(df2.pid, df2.resp_gend))
    caste2 = dict(zip(df2.pid, df2.caste))
    religion2 = dict(zip(df2.pid, df2.religion))


from collections import Counter


def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties, num_ties = 0, 0
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 > n2:  # do not double-count edges!
                if IDs[n1] in chars and IDs[n2] in chars:
                    if G.has_edge(n1, n2):
                        num_ties += 1
                        if chars[IDs[n1]] == chars[IDs[n2]]:
                            num_same_ties += 1
    return (num_same_ties / num_ties)


def make_test_colors():

    favorite_colors = {
        "ankit": "red",
        "xiaoyu": "blue",
        "mary": "blue"
    }

    # chance_homophily(favorite_colors)


if __name__ == '__main__':
    # test_birds_tudes()
    # test_birds_speed()
    # test_birds_speed_pandas()
    # test_birds_speed_datetime()
    # test_birds_speed_mean()
    # test_birds_sanne()
    # test_birds_speed_plot()
    # test_graphs_networks()    
    # test_graphs_karate()
    # test_erdos_renyi()
    # test_graph_degree()
    # test_graph_india()
    # test_graph_generator()
    make_dict_from_two_columns()
    make_test_colors()