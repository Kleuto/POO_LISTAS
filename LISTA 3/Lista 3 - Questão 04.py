softwares = ["Windows", "Chrome", "Word", "Excel", "Python"]

print("Lista original:", softwares)

novo = input("Digite o nome do novo software: ")
softwares.append(novo)

softwares.pop(1)

print("Lista após as alterações:", softwares)