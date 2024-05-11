import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from graph import G

print('\nСписок всіх міст: ', G.nodes())
print('\nСписок всіх міжміських шляхів: ', G.edges())
print("\nМіста, напряму пов'язані з Києвом: ", list(G.neighbors("Kyiv")))

# Degree Centrality
degree_centrality_dict = nx.degree_centrality(G)
degree_centrality_list = list(degree_centrality_dict.items())
sorted_degree_centrality = sorted(degree_centrality_list, key=lambda item: item[1], reverse=True)
print('\nСтупінь центральності (Degree Centrality):')
df = pd.DataFrame(sorted_degree_centrality, columns=['Місто', 'Ступінь центральності'])
print(df)

# Closeness Centrality
closeness_centrality_dict = nx.closeness_centrality(G)
closeness_centrality_list = list(closeness_centrality_dict.items())
closeness_centrality = sorted(closeness_centrality_list, key=lambda item: item[1], reverse=True)
print("\nБлизькість вузла (Closeness Centrality)")
cf = pd.DataFrame(closeness_centrality, columns=['Місто', 'Близькість вузла'])
print(cf)

# Closeness Centrality
betweenness_centrality_dict = nx.betweenness_centrality(G)
betweenness_centrality_list = list(betweenness_centrality_dict.items())
betweenness_centrality = sorted(betweenness_centrality_list, key=lambda item: item[1], reverse=True)
print("\nБлизькість вузла (Closeness Centrality)")
cf = pd.DataFrame(betweenness_centrality, columns=['Місто', 'Близькість вузла'])
print(cf)


nx.draw(G, with_labels=True)
plt.show()