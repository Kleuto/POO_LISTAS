soma = 0
quantidade = 0

for numero in range(1, 20):
    if numero % 2 == 0:
        soma += numero
        quantidade += 1

media = soma / quantidade

print(f"A média dos identificadores é: {media:.2f}")