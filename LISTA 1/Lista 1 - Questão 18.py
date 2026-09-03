tensao = float(input("Digite o valor da tensão (em volts): "))
corrente = float(input("Digite o valor da corrente (em amperes): "))

potencia = tensao * corrente

print(f"O valor da potência é: {potencia:.2f} watts")