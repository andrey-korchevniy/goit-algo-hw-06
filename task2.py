from graph import G
import networkx as nx
from collections import deque


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print('\nВідвідуємо вершину', vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print('\nВідвідуємо вершину ', vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


# Виклик функції DFS
print('\nАлгоритм DFS')
dfs_recursive(G, 'Kyiv')
print('\nАлгоритм робить обхід з Києва та триває в глибину до наступних міст, опрацьовуючи відповідну "гілку", далі починає з нової гілки')

# Запуск алгоритму BFS
print('\n\nАлгоритм BFS')
bfs_iterative(G, 'Kyiv')
print('\nАлгоритм робить обхід з Києва та опрацьовує спочатку найближчі міста, далі опрацьовує більш віддалені')