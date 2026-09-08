maior = float(input("Digite o 1º valor: "))

for i in range(2, 16):
    valor = float(input(f"Digite o {i}º valor: "))

    if valor > maior:
        maior = valor

print(f"O maior valor observado foi: {maior:.2f}")