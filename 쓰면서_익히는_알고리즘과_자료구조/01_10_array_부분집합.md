# 부분 집합
고유한 정수의 집합으로 배열이 주어지면 가능한 모든 부분집합을 반환하자. 중복된 부분집합은 허용하지 않는다.

입력으로 [1, 2, 3]이 주어지면, 결과로 [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]을 반환하면 된다.

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 정수형 배열.  
- 부분집합은 중복되지 않는다.
- 2차원 배열로 반환한다.

아이디어 (재귀)
- 모르겠음...
```

### 문제 풀이
```python

```

<br>
<br>

## 학습 후

### 문제 풀이
```python
def subsets_recursion(nums: list[int], res: list[list[int]], subset: list[int], idx: int):
  if len(subset) > len(nums):
    return

  res.append(subset[:])

  for i in range(idx, len(nums)):
    subset.append(nums[i])
    subsets_recursion(nums, res, subset, i + 1)
    subset.pop()

```

