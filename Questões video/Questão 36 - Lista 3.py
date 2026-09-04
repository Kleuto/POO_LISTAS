#O setor de TI precisa de um sistema para gerenciar os equipamentos
#enviados para manutenção. Para cada equipamento, deverão ser armazenados o nome e o
#custo estimado do reparo. Desenvolva um programa em Python que implemente um
#CRUD (Create, Read, Update e Delete) e utilize modularização, separando as principais
#funcionalidades do sistema em funções.
#O programa deverá permitir:
#Cadastrar um novo equipamento e seu custo estimado de reparo;
#Listar todos os equipamentos cadastrados;
#Atualizar os dados de um equipamento existente;
#Excluir um equipamento cadastrado;
#Exibir o equipamento que possui o maior custo estimado de reparo;
#Salvar os dados em um arquivo no formato CSV;
#Carregar os dados do arquivo CSV quando o programa for iniciado.
#Para aplicar o conceito de modularização, cada operação deverá ser implementada em
#uma função.

import csv


# Carrega os dados do arquivo CSV
def carregar_dados():
    equipamentos = []

    try:
        with open("equipamentos.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for equipamento in leitor:
                equipamento["custo"] = float(equipamento["custo"])
                equipamentos.append(equipamento)

    except FileNotFoundError:
        pass

    return equipamentos


# Salva os dados no arquivo CSV
def salvar_dados(equipamentos):
    with open("equipamentos.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "custo"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(equipamentos)


# Cadastra um novo equipamento
def cadastrar(equipamentos):
    nome = input("Digite o nome do equipamento: ")
    custo = float(input("Digite o custo estimado do reparo: R$ "))

    equipamento = {
        "nome": nome,
        "custo": custo
    }

    equipamentos.append(equipamento)
    salvar_dados(equipamentos)

    print("Equipamento cadastrado com sucesso!")


# Lista os equipamentos cadastrados
def listar(equipamentos):
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    for equipamento in equipamentos:
        print(
            "Nome:", equipamento["nome"],
            "| Custo: R$", equipamento["custo"]
        )


# Atualiza um equipamento
def atualizar(equipamentos):
    nome = input("Digite o nome do equipamento que deseja atualizar: ")

    for equipamento in equipamentos:
        if equipamento["nome"] == nome:
            novo_nome = input("Digite o novo nome: ")
            novo_custo = float(input("Digite o novo custo: R$ "))

            equipamento["nome"] = novo_nome
            equipamento["custo"] = novo_custo

            salvar_dados(equipamentos)

            print("Equipamento atualizado com sucesso!")
            return

    print("Equipamento não encontrado.")


# Exclui um equipamento
def excluir(equipamentos):
    nome = input("Digite o nome do equipamento que deseja excluir: ")

    for equipamento in equipamentos:
        if equipamento["nome"] == nome:
            equipamentos.remove(equipamento)
            salvar_dados(equipamentos)

            print("Equipamento excluído com sucesso!")
            return

    print("Equipamento não encontrado.")


# Mostra o equipamento com maior custo
def maior_custo(equipamentos):
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    equipamento = max(equipamentos, key=lambda x: x["custo"])

    print(
        "Equipamento com maior custo:",
        equipamento["nome"],
        "| Custo: R$",
        equipamento["custo"]
    )


# Exibe o menu principal
def menu(equipamentos):
    while True:
        print("\n--- SISTEMA DE MANUTENÇÃO ---")
        print("1 - Cadastrar equipamento")
        print("2 - Listar equipamentos")
        print("3 - Atualizar equipamento")
        print("4 - Excluir equipamento")
        print("5 - Mostrar maior custo")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(equipamentos)

        elif opcao == "2":
            listar(equipamentos)

        elif opcao == "3":
            atualizar(equipamentos)

        elif opcao == "4":
            excluir(equipamentos)

        elif opcao == "5":
            maior_custo(equipamentos)

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


# Carrega os dados antes de iniciar
equipamentos = carregar_dados()

# Inicia o menu
menu(equipamentos)