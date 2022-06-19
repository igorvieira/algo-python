num = [1, 2, 3, 4, 5]
# [0,1,2,3,4]
counter_par = 0
counter_impar = 0


for n in num:
  if (n%2 == 0):
    print('Esse número é par: ', n)
    counter_par+=1
  else:
    print('Esse número é impar: ', n)
    counter_impar+=1

print("==================================")
print("Números pares", counter_par)
print("Números impares", counter_impar)

# Algoritmo

# for x = 0; x < 5; x ++ {
#  x = 0, 1, 2, 3, 4, 5
#  p = 2, 4
#  i = 1, 3, 5
#  cp = 1, 2
#  ci = 1, 2, 3
# }
