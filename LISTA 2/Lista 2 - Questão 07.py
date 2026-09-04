notas = []

try:
    quantidade = int(input("Digite quantas notas ira calcular: "))

    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / quantidade
    print(f"A média das notas é: {media:.2f}")

except ValueError:
    print("Entrada inválida! Digite números válidos.")
