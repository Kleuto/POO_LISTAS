valores = []

for i in range(7):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)

print("Valores na ordem inversa:", valores[::-1])