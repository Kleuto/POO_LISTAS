nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano_nasc

if idade < 18:
    print("Menores de idade precisam estar acompanhados de um responsável.")

else:
    print(f"Olá, {nome}! Você tem {idade} anos! Seu acesso está liberado.")
