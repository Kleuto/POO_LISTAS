menor = float(input("Digite a 1ª latência: "))

for i in range(2, 11):
    latencia = float(input(f"Digite a {i}ª latência: "))

    if latencia < menor:
        menor = latencia

print(f"A menor latência registrada foi: {menor:.2f} ms")