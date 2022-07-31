mx = [
    [2, 4, 5],
    [1, 3, 7],
    [6, 8, 9],
  ]

increment = 0
primary = 0

for row in mx:
  primary += row[increment]
  increment += 1

print(primary)