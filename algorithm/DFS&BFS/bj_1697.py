#
# 1697. 숨바꼭질
# https://www.acmicpc.net/problem/1697
#

from collections import deque

#
# Functions
#

def DFS(target) :
    global queue, visited, dx

    while queue :
        loc = queue.pop() # 현재 위치
        if loc == target : return
        newloc = [loc-1, loc+1, loc*2]

        for x in newloc :
            if 0 <= x <= 200000 and not visited[x] :
                visited[x] = visited[loc] + 1
                if x == target : return
                queue.appendleft(x)

#
# Main
#

start, end = map(int, input().split())

queue = deque([start])
visited = [0] * 200001
visited[start] = 1

DFS(end)
print(visited[end] - 1)