# 배열에서 다수의 요소 찾기
정수형 배열이 주어졌을 때 다수의 요소를 찾아보자. 다수의 요소는 배열 내에서 ```floor(n/2)```번을 초과하여 나타나는 요소를 말한다. 예를 들어 배열 요소 총개수가 9개라면 5이다. 배열은 항상 1개 이상의 요소를 가지고 있으며 다수의 수가 무조건 하나 존재한다고 가정하자.
<br>

- 입력값 : nums = [2, 1, 2]
<br>

## 학습 전
### 문제 접근
```text
제한사항
- 정수형 배열이다.
- 배열은 1개 이상의 요소를 가지고 있다.
- 다수의 수가 무조건 하나 존재한다.

아이디어
1. 해시테이블을 생성한다.
2. 정수형 배열을 순회한다.
  - 요소의 값이 해시테이블에 존재하면 값에 1을 증가한다.
  - 없다면, 키값으로 요소의 값을, 값에 1을 초기화한다.
  - 할당한 값이 n/2 를 초과하면 반환한다.
 
```

### 문제 풀이
```python
def majorityElement(nums: list[int]):
  hashTable = {}
  majorityCount = int(len(nums) / 2)

  for i, num in enumerate(nums):
    if hashTable.get(num) is None:
      hashTable[num] = 1
    else:
      hashTable[num] = hashTable[num] + 1

    if hashTable[num] > majorityCount:
      return num
```

<br>
<br>

## 학습 후
### 문제 접근
```text
아이디어
1. 배열을 정렬한다.
2. int(n/2) 번째 숫자를 반환한다.
```

### 문제 풀이
```python
def majorityElement(nums: list[int]):
  return sorted(nums)[int(len(nums) / 2)]
```

