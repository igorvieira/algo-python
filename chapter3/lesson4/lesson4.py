number_students = input("Digite o número de estudantes: ")

ns = int(number_students)
total_score = 0


for x in range(ns):
    print("Digite a ", x+1, "º ")
    score = input("Nota: ")
    parsed_score = float(score)

    if parsed_score > 0 and parsed_score < 10:
        total_score += parsed_score
    else:
        print("Valores fora maiores que 10 ou menores que 0")

        break

print(total_score/ns)
