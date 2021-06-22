import sys
from collections import deque

answers = [1,3,2,4,2]
num = len(answers)

supo1 = [1,2,3,4,5] * (num // 5 + 1)
supo2 = [2,1,2,3,2,4,2,5] * (num // 8 + 1)
supo3 = [3,3,1,1,2,2,4,4,5,5] * (num // 10 + 1)

res = []
for supo in [supo1, supo2, supo3] :
    res.append(sum(map(lambda x, y : x == y, answers, supo)))

maxi = max(res)
answer = []
for i in range(3) :
    if res[i] == maxi : answer.append(i+1)

