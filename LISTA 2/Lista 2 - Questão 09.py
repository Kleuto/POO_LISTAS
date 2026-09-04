notas = []

for i in range(5):
    while True:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota: "))
            notas.append(nota)
            break
        except ValueError:
            print("Entrada inválida. Digite um número.")

try:
    media = sum(notas) / len(notas)

    print("Notas:", notas)
    print("Média:", media)
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))

except ZeroDivisionError:
    print("Não há notas para calcular.")