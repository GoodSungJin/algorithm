# 배열에서 삽입 위치 찾기
정렬된 배열과 목푯값이 주어지는데 목푯값을 찾는다면 배열의 해당 인덱스를 반환하고, 찾지 못한다면 정렬된 배열이 되도록 목표값이 배열에 들어가야 하는 인덱스를 구하는 문제다.

- 입력값 : nums = [1, 2, 3, 4, 5], target = 3
- 출력값 : 2

- 입력값 : nums = [1, 4, 5, 6], target = 3
- 출력값 : 1

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 배열을 정렬되어 있다.

아이디어
1. 배열을 순차적으로 순회한다.
  - target <= nums[i]일 경우 i 를 반환한다.
```

### 문제 풀이
```python
def find_index(nums: list[int], target: int):
  i = 0

  while True:
    if target <= nums[i]:
      return i

    i += 1
```

<br>
<br>

## 학습 후
### 문제 접근
```text
제한사항
- 정수형 배열
- 정수형 target 변수
- 배열의 값은 정수, 즉 음수, 0, 양수를 포함한다.
- 배열은 정렬되어 있다.
- 배열의 크기는 매우 클 수 있다.

아이디어
1. 배열 요소를 이진 탐색으로 접근한다.
2. 요소를 찾는다면, 해당 인덱스를 반환
3. 끝까지 찾지 못하고 이진 탐색을 종료한다면, 최종 접근했던 낮은 인덱스의 값을 반환한다.
```

### 문제 풀이
```python
def search_insert(nums: list[int], target: int):
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = int((low + high) / 2)

    if nums[mid] < target:
      low = mid + 1
    elif nums[mid] > target:
      high = mid - 1
    else:
      return mid

    return low
```

