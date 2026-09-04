agenda = {}

for i in range(3):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")

    agenda[nome] = telefone

nome_solicitado = input("Digite o nome que deseja pesquisar: ")

if nome_solicitado in agenda:
    print("Telefone:", agenda[nome_solicitado])
else:
    print("Contato não encontrado.")