vogais = 0
consoantes = 0

for i in range(10):
    letra = input(f"Digite a {i + 1}ª letra: ")

    if letra.lower() in "aeiou":
        vogais += 1
    else:
        consoantes += 1

print(f"Quantidade de vogais: {vogais}")
print(f"Quantidade de consoantes: {consoantes}")