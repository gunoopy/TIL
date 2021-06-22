#
# 1707. 이분 그래프
# https://www.acmicpc.net/problem/1707
#

import sys
from collections import deque

#
# Functions
#

def BFS(start) :
    global G, bipart
    queue = deque([start])
    bipart[start] = 1

    while queue :
        node = queue.pop()
        label = bipart[node]
        for x in G[node] :
            if bipart[x] == label : return False
            if not bipart[x] :
                bipart[x] = -label # 반대 부호로 저장
                queue.appendleft(x)
    else : return True



#
# Main
#

t = int(sys.stdin.readline())

for _ in range(t) :
    V, E = map(int, sys.stdin.readline().split())
    G = {i : [] for i in range(1, V+1)}
    bipart = [0] * (V+1) # Label : -1 또는 1

    for _ in range(E) :
        v1, v2 = map(int, sys.stdin.readline().split())
        G[v1].append(v2)
        G[v2].append(v1)

    # disconnected graph인 경우도 고려
    # ex) Vertex = {1,2,3,4}, Edge = {(2,3), (3,4), (4,2)}
    for start in range(1, V+1) :
        if not bipart[start] :
            result = BFS(start)
            if not result :
                print('NO')
                break
    else : print('YES')