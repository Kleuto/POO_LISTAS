potencia = float(input("Digite o valor da potência (em watts): "))
tensao = float(input("Digite o valor da tensão de funcionamento (em volts): "))

corrente = potencia / tensao

print(f"O valor da corrente é: {corrente:.2f} amperes")
