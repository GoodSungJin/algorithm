# 배열의 회전
입력으로 정수형 배열과 k 값이 주어지면, 각 요소를 우측으로 k 번 이동 및 회전을 해보자.<br>
k는 양의 정수이다.

예를 들어 nums 배열에 [1, 2, 3, 4]가 있고, k가 1이라면 요소는 우측으로 1칸씩 이동 및 회전 하여 [4, 1, 2, 3]이 된다.

<br>

- 입력값 : nums = [1, 2, 3, 4], k = 1

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 정수형 배열 nums.  
- 양의 정수 k.

아이디어
1. 배열을 뒤집는다.
2. 첫번째 요소만 빼고 나머지 배열을 뒤집는다.
3. 1번, 2번을 k번 만큼 반복한다.
 
```

### 문제 풀이
```python
def test(nums: list[int], k: int):
  move = nums

  for i in range(k):
    reversedNums = move[::-1]

    move = reversedNums[:1] + reversedNums[1::][::-1]
  return move
```

<br>
<br>

## 학습 후
### 문제 접근
```text
아이디어
1. 모든 요소가 한 번씩 교환이 될 때까지 배열을 순회한다.
2. 요소를 k만큼 이동 및 저장한다.
  - 이동한 위치의 이전 요소는 저장한다.
  - 저장한 요소는 다음 k 만큼 이동하여 넣는다.
  - 시작한 요소까지 값을 이동시키면 해당 순회를 종료한다.
  - 이동시킬 때마다 카운트한다.
  - 다음 요소를 선택하고 다시 2번의 내용을 반복한다.
```

### 문제 풀이
```python
def rotation(nums: list[int], k: int):
  count = 0

  for start in range(k):
    if count >= len(nums):
      break
    prev_index = start
    prev_num = nums[start]

    while True:
      next_index = (prev_index + k) % len(nums)
      temp_num = nums[next_index]
      nums[next_index] = prev_num
      prev_num = temp_num

      prev_index = next_index
      count += 1

      if prev_index == start:
        break

  return nums
```

