soma = 0
contador = 0

while contador < 10:
    numero = int(input(f"Digite o {contador + 1}º código divisível por 3: "))

    if numero % 3 == 0:
        soma += numero
        contador += 1

print(f"A soma dos valores é: {soma}")