#
# 1260. DFS와 BFS
#

from collections import deque

deq = deque([1,2,3,4,5])

deq.rotate(2) # [4,5,1,2,3]

deq.rotate(-2) # [1,2,3,4,5]


print(deq)