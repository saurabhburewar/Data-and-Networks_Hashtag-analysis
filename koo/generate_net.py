import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def rekoo_net(data):
    G = nx.Graph()

    for index, row in data.iterrows():

        curr_user = row['username']
        if curr_user not in G:
            G.add_node(curr_user, weight=1)
        else:
            G.nodes[curr_user]['weight'] += 1

        if not pd.isna(row['rekoo_users']):
            s = row['rekoo_users']
            rekoo_list = s.strip('][').split(', ')

            for i in range(len(rekoo_list)):
                rekoo_list[i] = rekoo_list[i].strip("''")

            for rekoo_user in rekoo_list:
                if rekoo_user not in G:
                    G.add_node(rekoo_user, weight=1)
                else:
                    G.nodes[rekoo_user]['weight'] += 1

                if G.has_edge(curr_user, rekoo_user):
                    G[curr_user][rekoo_user]['weight'] += 1
                else:
                    G.add_edge(curr_user, rekoo_user, weight=1)

    nx.write_edgelist(G, "graph_edgelist.csv", delimiter=',')
    fig = plt.figure(1, figsize=(200, 100), dpi=60)
    # pos = nx.nx_agraph.graphviz_layout(G, prog='neato')
    # pos = nx.spring_layout(G, k=0.1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, node_color='#ffdf06', edge_color='#d4b900')
    fig.set_facecolor('black')
    plt.savefig("covid_graph.png")


def hash_net(data):
    H = nx.Graph()

    for index, row in data.iterrows():

        h_string = row['hashtags']
        h_list = h_string.strip('][').split(', ')

        for i in range(len(h_list)):
            h_list[i] = h_list[i].strip("''")
            h_list[i] = h_list[i].strip('#')

        for hashtag in h_list:
            if hashtag not in H:
                H.add_node(hashtag, weight=1)
            else:
                H.nodes[hashtag]['weight'] += 1

        for i in range(0, len(h_list)-1):
            for j in range(i+1, len(h_list)):
                u1 = h_list[i]
                u2 = h_list[j]
                if H.has_edge(u1, u2):
                    H[u1][u2]['weight'] += 1
                else:
                    H.add_edge(u1, u2, weight=1)

    nx.write_edgelist(H, "hash_edgelist.csv", delimiter='@')
    fig = plt.figure(1, figsize=(200, 100), dpi=60)
    pos = nx.spring_layout(H)
    nx.draw(H, pos=pos, node_color='#ffdf06', edge_color='#d4b900')
    fig.set_facecolor('black')
    plt.savefig("covid_hash.png")


data = pd.read_csv('./covid19/covid_data.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)


# rekoo_net(data)
hash_net(data)

# G1 = nx.read_edgelist('./graph_edgelist.csv', delimiter=',')
# fig = plt.figure(1, figsize=(200, 100), dpi=60)
# pos = nx.spring_layout(G1)
# nx.draw(G1, pos=pos, node_color='#ffdf06', edge_color='#d4b900')
# fig.set_facecolor('black')
# plt.savefig("covid_hash1.png")
