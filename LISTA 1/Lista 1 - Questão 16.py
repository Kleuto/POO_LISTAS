tensao = float(input("Digite o valor da tensão (em volts): "))
corrente = float(input("Digite o valor da corrente (em amperes): "))

resistencia = tensao / corrente

print(f"O valor da resistência é: {resistencia:.2f} ohms")
