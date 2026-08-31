n = float(input("Digite o valor de n: "))
x = float(input("Digite o valor de x: "))
resultado = n ** x
if n <= 0 or x <= 0:
    print("O número não pode ser zero ou negativo.")
else:
    
    print(f"O resultado de {n:.0f} elevado a {x:.0f} é: {resultado:.0f}")