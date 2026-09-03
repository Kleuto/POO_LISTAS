nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

p1 = float(input("Digite o peso da primeira nota: "))
p2 = float(input("Digite o peso da segunda nota: "))

media = (nota1*p1 + nota2*p2) / (p1+p2)

print(f"A média ponderada das notas é: {media:.2f}")

