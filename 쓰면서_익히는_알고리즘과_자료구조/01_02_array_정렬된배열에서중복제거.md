# 정렬된 배열에서 중복 제거
정렬된 배열의 요소들을 중복 없이 단 1번씩만 가질 수 있도록 주어진 배열을 <b>그대로</b> 수정하고, 수정된 배열의 새로운 길이를 반환하라.<br>
&#42; 추가적인 배열의 할당은 하지 않고, 중복된 요소를 하나만 남기고 걸러내는 함수를 만드는 것이다. 반환된 길이 이후에 있는 데이터는 무시해도 무방하다.

- 입력값 : nums = [0, 0, 0, 1, 2, 2]

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 배열을 그대로 수정한다. (들어온 nums를 수정한다.)
- 새로운 배열을 만들지 않는다.
- 배열을 정렬되어 있다.

아이디어
1. 현재 값(i)과 다음 값(i + 1)을 비교하며 제거한다.
  - 현재 값(i)과 다음 값(i + 1)이 같으면 다음 값을 지우고 다시 다음 값(i + 1)과 비교한다.
  - 다르면 현재 값에 +1을 더해 다음으로 넘어간다.
```

### 문제 풀이
```python
def remove_duplicates(nums: list[int]):
  i = 0

  while i != len(nums) - 1:
    currNum = nums[i]
    nextNum = nums[i + 1]

    if currNum == nextNum:
      nums.remove(currNum)
    else:
      i = i + 1

  return len(nums)
```

<br>
<br>

## 학습 후
### 문제 접근
```text
제한사항
- 정수형 배열
- 입력으로 주어지는 배열의 길이는 0 일 수도 있다.
- 반환값은 정수이며, 배열의 길이보다 작거나 같다.

아이디어
1. 맨 첫 요소(curr)를 저장한다.
2. 배열의 요소를 맨 첫 요소를 제외하고 순회한다.
  - 1에서 n - 1까지 순회
  - curr과 값이 같다면 다음 요소로 넘어간다
  - curr과 값이 같지 않다면, curr을 현재 값으로 업데이트하고 count 값을 하나 증가시킨다.
  - count 값을 증가시키기 전에 count가 인덱스가 되어 해당 공간에 달라진 curr 값으로 업데이트한다.
```

### 문제 풀이
```python
def remove_duplicates(nums: list[int]):
  if len(nums) <= 0:
    return 0

  curr = nums[0]
  cnt = 1

  for i in range(1, len(nums)):
    if curr != nums[i]:
      curr = nums[i]
      nums[cnt] = curr
      cnt += 1

  return cnt
```

