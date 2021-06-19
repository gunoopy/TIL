#
# 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178
#

from sys import stdin
from collections import deque

#
# Functions
#

def BFS() :
    global G, visited, N, M
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque([(0,0)])
    visited[0][0] = 1

    while queue :
        X, Y = queue.pop()
        if X == N-1 and Y == M-1 :
            break
        for i in range(4) :
            newX, newY = X + dx[i], Y + dy[i]
            if 0 <= newX < N and 0 <= newY < M and G[newX][newY] and not visited[newX][newY] :
                queue.appendleft((newX, newY))
                visited[newX][newY] = visited[X][Y] + 1

    print(visited[N-1][M-1])


#
# Main
#


N, M = map(int, stdin.readline().split()) # N x M matrix
G = []
visited = [[0]*M for _ in range(N)]

for _ in range(N) :
    G.append(list(map(int, list(stdin.readline().strip()))))

BFS()