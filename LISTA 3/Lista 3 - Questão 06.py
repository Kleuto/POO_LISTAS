numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

inicio = min(numero1, numero2)
fim = max(numero1, numero2)

for numero in range(inicio, fim + 1):
    print(numero)