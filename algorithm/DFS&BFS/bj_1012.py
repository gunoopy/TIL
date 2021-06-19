#
# 1012. 유기농 배추
# https://www.acmicpc.net/problem/1012
#

from sys import stdin
from collections import deque

#
# Functions
#

def BFS(start_row, start_col) :
    global G, visited, dx, dy, rows, cols
    queue = deque([(start_row, start_col)])
    while queue :
        X, Y = queue.pop()
        if not visited[X][Y] :
            visited[X][Y] = 1
            # 상하좌우 확인
            for i in range(4) :
                newX, newY = X + dx[i], Y + dy[i]
                # 정상 범위, 배추 심어진 땅, 아직 방문 전인 경우
                if 0 <= newX < rows and 0 <= newY < cols and G[newX][newY] and not visited[newX][newY] :
                    queue.appendleft((newX, newY))


#
# Main
#

t = int(input())
# 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for _ in range(t) :
    cols, rows, K = map(int, stdin.readline().split())
    G = [[0]*cols for _ in range(rows)]
    visited = [[0]*cols for _ in range(rows)]
    cnt = 0
    for _ in range(K) :
        col, row = map(int, stdin.readline().split())
        G[row][col] = 1

    for row in range(rows) :
        for col in range(cols) :
            if G[row][col] and not visited[row][col] :
                BFS(row, col)
                cnt += 1

    print(cnt)