def hanoi_tower(n, start, finish):
  middle = 6 - start - finish

  if n == 1:
    return print(start, finish)

  hanoi_tower(n - 1, start, middle)
  print(start, finish)
  hanoi_tower(n - 1, middle, finish)
