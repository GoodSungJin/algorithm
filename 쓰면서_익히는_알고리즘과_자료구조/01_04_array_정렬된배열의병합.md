# 정렬된 배열의 병합
주어진 정렬된 두 배열(nums1, nums2)을 정렬을 유지하면서 병합해보자.<br>

- 추가 설명:
  - nums1과 nums2의 각각의 크기는 m과 n개의 요소로 초기화되어 있다.
  - nums1은 nums1과 nums2를 병합하기에 충분한 크기로 할당되어 있다. (m + n 개)

<br>

- 입력값 : nums1 = [1, 2, 3, 0, 0, 0], nums2 = [2, 5, 6]

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 정렬된 배열이다.
- nums1 m개, nums2는 n개 이다
- nums1의 배열의 크기는 m + n 이다

아이디어
1. nums1에 nums2를 병합하고, 정렬한다.
```

### 문제 풀이
```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int):
  for i in range(len(nums2)):
    nums1[i + m] = nums2[i]

  return sorted(nums1)
```

<br>
<br>

## 학습 후
### 문제 접근
```text
아이디어 (비교 및 삽입)
1. nums1을 위한 포인터 i, nums1의 마지막 요소를 가리킴 (m - 1)
2. nums2을 위한 포인터 j, nums2의 마지막 요소를 가리킴 (n - 1)
3. 삽입을 위한 포인터 k, nums1 공간 마지막을 가리킴 (m + n - 1)
4. i와 j의 값을 비교한다.
  - 비교하여 큰쪽의 값을 k의 위치에 삽입한다.
  - 삽입했으니 k를 1 감소한다.
  - 삽입한 큰쪽의 인덱스를 1감소한다.
5. i와 j중 한 쪽이라도 0보다 작아지면 중지한다.
6. j가 0보다 크다면 k를 1감소하며 nums1에 삽입한다.
```

### 문제 풀이
```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int):
  i = m - 1
  j = n - 1
  k = m + n - 1

  while i >= 0 and j >= 0:
    if nums1[i] < nums2[j]:
      nums1[k] = nums2[j]
      j -= 1
    else:
      nums1[k] = nums1[i]
      i -= 1

    k -= 1

  while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

  return nums1
```

