# sys.stdin.readline()

> 반복문으로 여러줄을 입력 받을 때 사용
>
> 한 줄 단위로 입력
>
> 개행 문자가 같이 입력
>
> 파이썬에서 작은 시간 복잡도로 활용

<br/>

### 1) 개행문자 포함

```python
import sys

L = []

for i in range(3) :
    L.append(sys.stdin.readline()) # 'a', 'b', 'C' 입력

print(L) # ['a\n', 'b\n', 'c\n']
```

<br/>

<br/>

### 2) 형 변환

```python
import sys

a, b = map(int, sys.stdin.readline().split()) # '1 2' 입력

print(a, b) # 1 2
```

