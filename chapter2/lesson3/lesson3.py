"""
Created on Sat Dec 13 2021

@author: Vieira
Conceito por média de notas
Entre 9 a 10 nota A
Entre 8 a 9 nota B
Entre 7 a 8 nota C
Entre 6 a 7 nota D
Entre 5 a 6 nota F
"""

num1 = input("Digite um primeiro valor: ")
num2 = input("Digite um segundo valor: ")
num3 = input("Digite um terceiro valor: ")
num4 = input("Digite um quarto valor: ")

result = (float(num1) + float(num2) + float(num3) + float(num4))/4

if result>=9.0 and result<=10.0:
  print("Nota excelente! Mensão A")
  print("Resultado: ", result)
elif result>=8.0 and result<=9.0:
  print("Nota boa! Mensão B")
  print("Resultado: ", result)
elif result>=7.0 and result<=8.0:
  print("Nota satisfatória, mensão C")
  print("Resultado: ", result)
elif result>=6.0 and result<=7.0:
  print("Você passou raspando, mensão D =/")
  print("Resultado: ", result)
else:
  print("Você não passou, mensão F =/")
  print("Resultado: ", result)




