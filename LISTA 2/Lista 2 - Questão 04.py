soma_impares = 0

for i in range(1, 11):
    if i % 2 != 0:
        soma_impares += i

print(f"A soma dos números ímpares de 1 a 10 é: {soma_impares}")