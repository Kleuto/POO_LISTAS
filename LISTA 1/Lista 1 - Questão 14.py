numero_produtos = int(input("Digite o número de produtos: "))
produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto (em R$): "))

valor_total = produto * numero_produtos

valor_desconto = valor_total - desconto

print(f"O valor total a ser pago é: R$ {valor_desconto:.2f}")
