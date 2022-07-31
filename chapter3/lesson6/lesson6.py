num = input('Digite quantas iterações teremos: ')
minimum = 0

for x in range(int(num)):
  print('Digite a ', x+1, 'º ')
  value = input('valor: ')

  receive = int(value)

  if x == 0:
    minimum = receive
  elif receive < minimum:
    minimum = receive

print('O menor número: ', minimum)


# for x = 0; x < 3; x++
#   x = 0, 1, 2, 3
#   v = 2, 1, 3
#   m = 0, 2, 1
