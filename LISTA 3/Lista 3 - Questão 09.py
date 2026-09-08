inicio = int(input("Digite o primeiro identificador: "))
fim = int(input("Digite o último identificador: "))

soma = 0
quantidade = 0

for numero in range(min(inicio, fim), max(inicio, fim) + 1):
    soma += numero
    quantidade += 1

media = soma / quantidade

print(f"A média dos números é: {media:.2f}")