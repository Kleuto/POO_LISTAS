valores = []

for i in range(5):
    valor = float(input(f"Digite a {i + 1}ª medição: "))
    valores.append(valor)

print(f"A soma dos valores é: {sum(valores):.2f}")