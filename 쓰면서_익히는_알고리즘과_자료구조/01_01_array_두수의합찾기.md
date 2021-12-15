# 두 수의 합 찾기
주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값(target)을 만들 때, 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램을 작성하라. 입력값으로 주어지는 배열에는 정확히 하나의 정답이 존재하며, 같은 요소의 값을 중복해서 사용할 수 없다.

- 입력값 : nums = [2, 7, 10, 19], target = 9
- 출력값 : [0, 1]

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 주어진 배열에 정확히 하나의 정답이 존재한다.
- 같은 요소의 값을 중복해서 사용할 수 없다.

아이디어
1. 배열의 모든 요소의 조합을 찾는다.
  - i = 0 ~ n, j = i + 1 ~ n 2중 루프를 사용하여 구성한다.
```

### 문제 풀이
```python
def two_sum(nums, target):
  for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]


print(two_sum([2, 7, 10, 19], 9))
print(two_sum([8, 2, 11, 7], 9))
```

<br>
<br>

## 학습 후
### 문제 접근
```text
아이디어
1. Hash Table
  - target - 요소의 값 = 다른 값
  - 다른 값이 해시테이블에 없으면 요소의 값은 키 값으로, 요소의 인덱스를 값으로 해시테이블에 추가한다.
  - 다른 값이 해시테이블에 있으면 현재 요소의 인덱스와 다른 값의 인덱스(값)을 반환한다. 
```

### 문제 풀이
```python
def two_sum(nums, target):
  hash_table = {}

  for i in range(0, len(nums)):
    value = target - nums[i]

    if hash_table.get(value) is not None\
        and hash_table[value] != i:
      return [hash_table[value], i]

    hash_table[nums[i]] = i


print(two_sum([2, 7, 10, 19], 9))
print(two_sum([8, 2, 11, 7], 9))
```

