import json
from collections import deque

class Graph:

    def __init__(self):
        self.adjacency_list = json.load(open('graph.json'))

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # 모든 노드에 대해 동일한 값을 갖는 휴리스틱 함수
    def h(self, n): return 1

    def a_star_algorithm(self, start_node, stop_node):
        
        # open_list : 최단경로를 분석하기 위한 상태 
        # closed_list : 처리가 완료된 노드
        open_list = set([start_node])
        closed_list = set([])

        # g : 시작점 노드에서 현재 노드까지 거리 
        # 기본값 (지도에서 찾을 수 없는 경우) : 무한대 
        g = {}

        g[start_node] = 0

        # parents : 인접한 노드 (직전 노드)
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # f 값이 가장 낮은 노드 찾기
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # 현재 노드가 도착점이면,
            # 시작점에서부터 도착점까지 경로 재구성
            if n == stop_node:
                reconst_path = []
                path_len = 0
                
                while parents[n] != n:          #도착점부터 직전 노드를 따라가면서 시작점까지 
                    reconst_path.append(n)
                    n = parents[n]              #직전 노드

                reconst_path.append(start_node)
                reconst_path.reverse()          #반대로 추적했기 때문
                
                print('Path found: {}'.format(reconst_path))

                return reconst_path


            # 현재 노드의 인접한 모든 노드에 대해 수행
            for (m, weight) in self.get_neighbors(n):
                
                # 현재 노드가 open_list와 closed_list에 모두 없는 경우 
                # open_list에 노드 추가
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # 그렇지 않은 경우, 먼저 n을 방문하는 것이 빠른지 확인하고, 그 다음 m 방문
                # 부모 데이터와 g 데이터를 업데이트
                # 노드가 closed_list에 있으면 open_list로 이동
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # open_list에서 n을 제거하고 closed_list에 추가
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

graph1 = Graph()
graph1.a_star_algorithm('194041', '106906')