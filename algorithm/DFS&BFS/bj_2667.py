#
# 2667. 단지번호 붙이기
# https://www.acmicpc.net/problem/2667
#

import sys
from collections import deque

#
# Functions
#

def BFS(row, col) :
    global G, visited, dx, dy, N, counts
    cnt = 0
    queue = deque([(row,col)])
    while queue :
        X, Y = queue.pop()
        if not visited[X][Y] :
            visited[X][Y] = 1
            cnt += 1
            # 상하좌우 확인
            for i in range(4) :
                newX = X + dx[i]
                newY = Y + dy[i]
                # newX, newY가 범위 내, 집이 있는 곳, 아직 방문 전인 경우
                if 0 <= newX < N and 0 <= newY < N and G[newX][newY] and not visited[newX][newY] :
                    queue.appendleft((newX, newY))

    counts.append(cnt)

#
# Main
#

N = int(input())
G = []
visited = [[0]*N for _ in range(N)]
counts = []

# 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N) :
    G.append(list(map(int, list(input()))))

for row in range(N) :
    for col in range(N) :
        if G[row][col] and not visited[row][col] :
            BFS(row, col)


print(len(counts))
for cnt in sorted(counts) :
    print(cnt)