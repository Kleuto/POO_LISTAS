resistencia = float(input("Digite o valor da resistência (em ohms): "))
tensao = float(input("Digite o valor da tensão (em volts): "))

corrente = tensao / resistencia

print(f"O valor da corrente é: {corrente:.2f} amperes")