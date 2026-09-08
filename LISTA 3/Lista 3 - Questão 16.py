inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

quantidade = 0

for numero in range(min(inicio, fim), max(inicio, fim) + 1):
    if numero % 7 == 0:
        quantidade += 1

print(f"Quantidade de múltiplos de 7: {quantidade}")