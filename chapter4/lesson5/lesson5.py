mx = [
    [2, 4, 5],
    [1, 3, 7],
    [6, 8, 9],
  ]

decrement = len(mx)-1
secondary = 0

for row in mx:
  secondary += row[decrement]
  decrement -= 1

print(secondary)