num = input("Digite um número: ")

# for x in range(1, int(num) + 1):
#   if (x %2 == 0):
#     print("Números pares: ", x)
#   else:
#     print("Números impares: ", x)

for x in range(int(num)):
  if x %2 == 0 :
    print("Números pares: ", x)
  else:
    print("Números impares: ", x)
