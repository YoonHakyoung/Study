import json
from collections import deque
class Graph:
    def __init__(self):
        self.adjacency_list = json.load(open('adList(w).json'))
        self.adjacency_list_real = json.load(open('adList.json'))
        self.wktlist = json.load(open('adList(wkt).json'))
    def get_neighbors(self, v):
        return self.adjacency_list[v]
    def h(self, n): return 1
    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                reconst_path = []
                path_wkt = []
                path_len = 0
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                for i in range(len(reconst_path)-1):
                    current_node = reconst_path[i]
                    next_node = reconst_path[i+1]
                    for (neighbor, weight) in self.get_neighbors(current_node):
                        if neighbor == next_node:
                            for (neighbor_real, weight_real) in self.adjacency_list_real[current_node]:
                                if neighbor_real == neighbor:
                                    path_len += weight_real
                            break
                for pathnode in reconst_path:
                    path_wkt.append(self.wktlist[pathnode])
                print('Path found: {}\nTotal distance: {}\nlati,longi: {}'.format(reconst_path, path_len, path_wkt))
                return reconst_path
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

graph1 = Graph()
graph1.a_star_algorithm('194041', '106906')