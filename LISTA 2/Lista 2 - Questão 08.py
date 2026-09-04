notas = [3.0, 6.5, 7.5, 5.0, 9.0, 4.5, 7.0, 8.5, 6.0, 10.0]

aprovados = 0

for nota in notas:
    if nota >= 7.0:
        aprovados += 1

print("Quantidade de estudantes aprovados:", aprovados)