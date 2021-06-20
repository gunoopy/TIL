import sys
from collections import deque

queue = deque()

queue.appendleft((1,1))
print(queue)


a = [[1,1,2], [3,4,5], [7,8,1]]

print(True in (map(lambda x : 0 in x, a)))

# if sum([False, False]) : print('dsa')