equipamentos = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º equipamento: ")
    preco = float(input(f"Digite o preço do {i + 1}º equipamento: "))

    equipamentos.append([nome, preco])

print("\nEquipamentos cadastrados:")

for equipamento in equipamentos:
    print(f"{equipamento[0]} - R$ {equipamento[1]:.2f}")

mais_caro = max(equipamentos, key=lambda equipamento: equipamento[1])

print(f"\nEquipamento mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}")