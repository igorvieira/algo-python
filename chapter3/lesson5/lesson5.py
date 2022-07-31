num = input('Digite quantas iterações teremos: ')
highster = 0


for x in range(int(num)):
  print("Digite a ", x+1, "º ")
  valor = input('valor: ')

  receive = int(valor)

  if x == 0:
    highster = receive
  elif receive > highster:
    highster = receive

print('O maior número: ', highster)

# Algoritmo

# for x = 0; x < 3; x++
#   x = 0, 1, 2, 3
#   v = 1, 3, 2
#   h = 1, 3
