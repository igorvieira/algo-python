"""
Created on Sat Dec 14 2021

@author: Vieira
A soma dos quadrados dos catetos que são iguais a
hipotenusa

Se houver um cateto, calcular o cateto adjacente
Se houver os dois catetos, calcular a hipotenusa
Para a ausência de qualquer cateto ou hipotenusa o valor deve ser zero
"""

import math

cat1 = input("Digite o primeiro cateto: ")
cat2 = input("Digite o segundo cateto: ")
hip = input("Digite a hipotenusa: ")

newCat1 = int(cat1)
newCat2 = int(cat2)
newHip = int(hip)

if newCat1 == 0:
  newCat1 = int(math.sqrt(pow(newHip, 2) +  pow(newCat2, 2)))
  print('Cateto 1 tem o valor de: ', newCat1)
elif newCat2 == 0:
  newCat2 = int(math.sqrt(pow(newHip, 2) +  pow(newCat1, 2)))
  print('Cateto 2 tem o valor de: ', newCat2)
else:
  newHip = int(math.sqrt(pow(newCat1, 2) +  pow(newCat2, 2)))
  print('Hipotenusa tem o valor de: ', newHip)






