opcao = input("Digite 1 para calcular a hipotenusa ou 2 para calcular o Cateto: ")

match opcao:
    case "1":
        cateto1 = float(input("Digite o valor do primeiro cateto: "))
        cateto2 = float(input("Digite o valor do segundo cateto: "))
        hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
        print(f"O valor da  hipotenusa é: {hipotenusa}")
    case "2":
        hipotenusa = float(input("Digite o valor da hipotenusa: "))
        outro_cateto = float(input("Digite o valor do outro cateto: ")) 
        cateto = (hipotenusa ** 2 - outro_cateto ** 2) ** 0.5
        print(f"O valor do cateto é: {cateto:.2f}")
    case _:
        print("Opção inválida.")