#
# 2606. 바이러스
# https://www.acmicpc.net/problem/2606
#

import sys
from collections import deque

def BFS(G) :
    queue = deque([1])
    visited = []
    while queue :
        node = queue.pop()
        if node not in visited :
            visited.append(node)
            queue.extend(G[node])

    print(len(visited) - 1)

V = int(input())
E = int(input())
G = {}.fromkeys(range(1, V+1))

for _ in range(E) :
    v1, v2 = map(int, sys.stdin.readline().split())

    if not G[v1] : G[v1] = [v2]
    else : G[v1].append(v2)

    if not G[v2] : G[v2] = [v1]
    else : G[v2].append(v1)


BFS(G)

