latencias = []
adequados = 0
lentos = 0

for i in range(10):
    latencia = float(input(f"Digite a latência do {i + 1}º teste: "))
    latencias.append(latencia)

    if latencia <= 100:
        adequados += 1
    else:
        lentos += 1

media = sum(latencias) / 10
maior = max(latencias)

print(f"Testes adequados: {adequados}")
print(f"Testes lentos: {lentos}")
print(f"Média das latências: {media:.2f} ms")
print(f"Maior latência: {maior:.2f} ms")