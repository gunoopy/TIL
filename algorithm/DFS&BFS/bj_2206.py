#
# 2206. 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
#

import sys
from collections import deque

#
# Functions
#

def BFS() :
    global G, visited, queue, rows, cols, dx, dy

    while queue :
        is_break, row, col = queue.pop()
        if row == rows-1 and col == cols-1 : return visited[is_break][row][col]

        # 상하좌우 탐색
        for i in range(4) :
            newX, newY = row + dx[i], col + dy[i]

            # 정상 범위
            if 0 <= newX < rows and 0 <= newY < cols :
                # target 도달
                if newX == rows-1 and newY == cols-1 :
                    return visited[is_break][row][col] + 1

                # 길 O, 방문 X
                if not G[newX][newY] and not visited[is_break][newX][newY] :
                    queue.appendleft((is_break, newX, newY))
                    visited[is_break][newX][newY] = visited[is_break][row][col] + 1
                # 길 X, 벽 부수기 전
                elif not is_break and G[newX][newY] :
                    queue.appendleft((1, newX, newY))
                    visited[1][newX][newY] = visited[is_break][row][col] + 1
    else : return -1 # 탐색 불가


#
# Main
#

rows, cols = map(int, sys.stdin.readline().split())
G = []
visited = [[[0]*cols for _ in range(rows)] for _ in range(2)]
visited[0][0][0] = 1
queue = deque([(0,0,0)])
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(rows) :
    G.append(list(map(int, list(sys.stdin.readline().strip()))))

print(BFS())
