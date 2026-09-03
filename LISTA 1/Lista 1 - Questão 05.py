placa = (input("Digite o número da placa do veículo: ").strip())
ultimo_digito = int(placa[-1])  
if ultimo_digito % 2 == 0:
    print("O veículo tem o final da placa Par e deve utilizar o portão A.")
else:
    print("O veículo tem o final da placa Ímpar e deve utilizar o portão B.")   