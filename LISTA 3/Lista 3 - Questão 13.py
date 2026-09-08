while True:
    temperatura = float(input("Digite a temperatura: "))

    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    print("5 - Fahrenheit para Kelvin")
    print("6 - Kelvin para Fahrenheit")

    opcao = int(input("Escolha a conversão: "))

    if opcao == 1:
        resultado = (temperatura * 9 / 5) + 32
    elif opcao == 2:
        resultado = (temperatura - 32) * 5 / 9
    elif opcao == 3:
        resultado = temperatura + 273.15
    elif opcao == 4:
        resultado = temperatura - 273.15
    elif opcao == 5:
        resultado = (temperatura - 32) * 5 / 9 + 273.15
    elif opcao == 6:
        resultado = (temperatura - 273.15) * 9 / 5 + 32
    else:
        print("Opção inválida.")
        continue

    print(f"Resultado: {resultado:.2f}")

    continuar = input("Deseja realizar outra conversão? (s/n): ")

    if continuar.lower() != "s":
        break