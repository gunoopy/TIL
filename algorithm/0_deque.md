# collections.deque

> double-ended queue
>
> 양방향에서 데이터를 처리할 수 있는 자료구조 (stack or queue)
>
> 파이썬에서 작은 시간 복잡도로 활용

<br/>

### 1) append & pop

```python
from collections import deque

deq = deque([3,4,5])

# Add element to the start
deq.appendleft(10) # [10,3,4,5]

# Add element to the end
deq.append(100) # [10,3,4,5,100]

# Pop element from the start
deq.popleft() # [3,4,5,100]

# Pop element from the end
deq.pop() # [3,4,5]
```

<br/>

<br/>

### 2) rotate

```python
from collections import deque

deq = deque([1,2,3,4,5])

deq.rotate(2) # [4,5,1,2,3]

deq.rotate(-2) # [1,2,3,4,5]
```



