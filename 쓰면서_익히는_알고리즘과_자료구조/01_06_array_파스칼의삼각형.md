# 파스칼의 삼각현
파스칼의 삼각형은 수학의 이항 계수를 삼각형의 형태로 숫자를 배열한 구성을 말한다. <br>
입력으로 몇 줄을 만들 것인지를 받아서 파스칼의 삼각형을 이차원 배열의 형태로 구성해보자.

## 학습 전
### 문제 접근
```text
제한사항
- 입력 값은 정수이다.
- 반환 값은 이차원배열이다.

아이디어
1. i 는 num 만큼 순회한다.
  - 이떄 첫번째는 무조건 1이기 떄문에 0번 인덱스는 빼고 시작한다.
2. j는 i + 1만큼 이중 순회한다.
  - 첫번째는 무조건 1이기 때문에 0번 인덱스를 빼고 시작한다.
  - i 보다 j 가 크면 이전요소를 참조할 때 에러가 나기 때문에 j < i 조건으로 이전 배열의 j - 1번째 요소와 이전배열의 j번째 요소를 더해서 넣어준다.
  - 조건에 맞지 않다면 1 넣어준다. 
```

### 문제 풀이
```python
def generate(num: int):
  if num == 0:
    return []

  array = [[1]]

  for i in range(1, num):
    row = [1]

    for j in range(1, i + 1):
      if j < i:
        prevNum = array[i - 1][j - 1]
        nextNum = array[i - 1][j]

        row.append(prevNum + nextNum)
      else:
        row.append(1)

    array.append(row)

  return array
```

<br>
<br>

## 학습 후
동일하다.

