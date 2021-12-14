"""
Created on Sat Dec 13 2021

@author: Vieira
Saber se o usuário passou ou não de ano (média de 7.5)
"""

num1 = input("Digite um primeiro valor: ")
num2 = input("Digite um segundo valor: ")
num3 = input("Digite um terceiro valor: ")
num4 = input("Digite um quarto valor: ")

result = (float(num1) + float(num2) + float(num3) + float(num4))/4

if result >= 7.5:
  print("Você passou!")
  print("Resultado: ", result)
else:
  print("Você não passou =/")
  print("Resultado: ", result)




