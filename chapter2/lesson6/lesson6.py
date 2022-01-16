"""
Created on Sun Jan 16 2022

@author: Vieira
Palíndromo
"""
word = input("Digite uma palavra: ")

worldWithOutSpaces = word.replace(' ', '')
wordWithLowerCase = worldWithOutSpaces.lower()
worldReverse = wordWithLowerCase[::-1]

if wordWithLowerCase == worldReverse:
  print('Isso é um palíndromo')
else:
  print('Isso não é um palindromo')