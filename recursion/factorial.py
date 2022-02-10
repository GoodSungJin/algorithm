def fact(num):
  if num == 1:
    return 1

  return fact(num - 1) * num
