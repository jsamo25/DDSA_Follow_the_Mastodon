import networkx as nx
import matplotlib.pyplot as plt

mastodon_digraph = nx.read_edgelist("mastodon_first_snapshot_anonim.csv", create_using= nx.DiGraph(),delimiter=",")

#To load the temporal annotated links:
with open("mastodon_growth_from_1_16_to_3_16_anonim.csv","r") as f:
    for line in f:
        source, destination, date = line.strip().split(",")
        mastodon_digraph.add_edge(source,destination,timestamp=date)


