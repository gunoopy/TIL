#
# 7576. 토마토
# https://www.acmicpc.net/problem/7576
#

from sys import stdin
from collections import deque

#
# Functions
#

def BFS() :
    global G, queue, cols, rows
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue :
        X, Y = queue.pop()
        days = G[X][Y]
        for i in range(4) : # 상하좌우 확인
            newX, newY = X + dx[i], Y + dy[i]
            if 0 <= newX < rows and 0 <= newY < cols and not G[newX][newY] : # 익지 않은 토마토
                G[newX][newY] = days + 1
                queue.appendleft((newX, newY))

#
# Main
#

cols, rows = map(int, input().split())
G = []
queue = deque()

for _ in range(rows) :
    G.append(list(map(int, stdin.readline().split())))

for i in range(rows) :
    for j in range(cols) :
        if G[i][j] == 1 : queue.appendleft((i, j))

BFS()

# 0(익지 않은 토마토)이 있는 경우
if True in map(lambda x : 0 in x, G) : print(-1)
else : print(max(map(max, G)) - 1) # 최대값