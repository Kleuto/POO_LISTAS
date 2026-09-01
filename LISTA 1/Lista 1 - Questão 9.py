lado_1 = float(input("Digite o comprimento do L1: "))
lado_2 = float(input("Digite o comprimento do L2: "))
lado_3 = float(input("Digite o comprimento do L3: "))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
   
    if lado_1 == lado_2 and lado_2 == lado_3 and lado_1 == lado_3:
        print("O triângulo é equilátero.")
    elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
        print("O triângulo é escaleno.")
    else:
        print("O triângulo não é equilátero nem escaleno.")

else:
    print("Os valores não formam um triângulo.")