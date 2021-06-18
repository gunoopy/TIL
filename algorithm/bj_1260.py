#
# 1260. DFS와 BFS
#

import sys
from collections import deque

def DFS(G, start) :
    stack = deque([start])
    visited = []
    while stack :
        node = stack.pop()
        if node not in visited : # 아직 방문 전인 경우만, 방문했다면 pop만
            visited.append(node)
            print(node, end = ' ')
            if G[node] : # path 존재하는 경우만
                stack.extend(sorted(G[node], reverse = True))
    else : print()


def BFS(G, start) :
    queue = deque([start])
    visited = []
    while queue :
        node = queue.pop()
        if node not in visited : # 아직 방문 전인 경우만, 방문했다면 pop만
            visited.append(node)
            print(node, end = ' ')
            if G[node] : # path 존재하는 경우만
                queue.extendleft(sorted(G[node]))






V, E, start = map(int, sys.stdin.readline().split())
G = {}.fromkeys(range(1, V+1))

for _ in range(E) :
    v1, v2 = map(int, sys.stdin.readline().split())

    if not G[v1] : G[v1] = [v2]
    else : G[v1].append(v2)

    if not G[v2] : G[v2] = [v1]
    else : G[v2].append(v1)


DFS(G, start)
BFS(G, start)