from graph import G
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

pos = nx.kamada_kawai_layout(G, weight='weight')

plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_size=1200, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


shortest_paths = nx.single_source_dijkstra_path(G, source='Kyiv')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Kyiv')

data = {
    'Пункт призначення': [],
    'Шлях': [],
    'Найкоротша відстань': []
}

for destination, path in shortest_paths.items():
    data['Пункт призначення'].append(destination)
    data['Шлях'].append(path)
    data['Найкоротша відстань'].append(shortest_path_lengths[destination])

df = pd.DataFrame(data)
print(df)