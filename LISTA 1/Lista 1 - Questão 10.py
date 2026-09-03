financiamento = float(input("Digite o valor do financiamento: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))
meses = int(input("Digite o número de meses para o financiamento: "))

juros_decimal = juros_mensal / 100
juros_total = financiamento * juros_decimal * meses
montante_total = financiamento + juros_total

print(f"O valor dos juros acumulados é: R$ {juros_total:.2f}")
print(f"O montante total a ser pago é: R$ {montante_total:.2f}")