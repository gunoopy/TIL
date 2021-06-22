#
# 7562. 나이트의 이동
# https://www.acmicpc.net/problem/7562
#

import sys
from collections import deque

#
# Functions
#

def BFS(G, I, startX, startY, endX, endY) :
    # 이동 없는 경우
    if startX == endX and startY == endY : return 0

    G[startX][startY] = 1
    queue = deque([(startX, startY)])

    # 나이트 이동 가능 위치
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [2,1,-1,-2,-2,-1,1,2]

    while queue :
        X, Y = queue.pop()
        for i in range(8) :
            newX, newY = X + dx[i], Y + dy[i] # 이동된 나이트 위치
            if newX == endX and newY == endY : return G[X][Y]

            # 정상 범위, 이동 안한 위치
            if 0 <= newX < I and 0 <= newY < I and not G[newX][newY] :
                G[newX][newY] = G[X][Y] + 1
                queue.appendleft((newX, newY))

#
# Main
#

t = int(sys.stdin.readline())

for _ in range(t) :
    I = int(sys.stdin.readline())
    startX, startY = map(int, sys.stdin.readline().split())
    endX, endY = map(int, sys.stdin.readline().split())

    G = [[0]*I for _ in range(I)]

    print(BFS(G, I, startX, startY, endX, endY))



