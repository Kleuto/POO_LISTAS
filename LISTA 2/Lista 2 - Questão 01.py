soma = 0
contador = 0

while contador < 10:
    numero = int(input(f"Digite o {contador + 1}º código divisível por 6: "))
    if numero % 6 == 0:
        soma += numero
        contador += 1
else:
    print("Valor inválido! digite um código divisível por 6.")

print(f"A soma dos números digitados é: {soma}")