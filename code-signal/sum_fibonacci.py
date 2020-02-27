# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

first = 0
second = 1
sum = 0

while second < 4000000:
  temp = first
  first = second
  second = temp + first

  if second % 2 == 0:
    sum += second

print(sum)