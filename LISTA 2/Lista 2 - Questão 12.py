quadrados = {}

for numero in range(1, 11):
    quadrados[numero] = numero ** 2

for chave, valor in quadrados.items():
    print(chave, ":", valor)