qtd_students = input('Digite o número de estudantes: ')

ns = int(qtd_students)
total_score = 0


for x in range(ns):
  print("Digite a ", x+1, "º: ")
  score =  input("Nota: ")
  parsed_score = float(score)

  if parsed_score > 0 and parsed_score < 10:
    total_score += parsed_score
  else:
    print("Digite valores maiores que 0 e menores que 10")
    break


print(total_score/ns)


# Algoritmo:

# for x = 0; x < 5; x++ {
#   x = 0, 1, 2, 3, 4, 5
#   t = 9, 8, 4, 7, 8
# }
