disciplina = {
    "nome": "POO",
    "professor": "Mário",
    "carga_horaria": 60,
    "periodo": 3
}

chave = input("Digite o nome da chave que deseja pesquisar: ")

if chave in disciplina:
    print(f"A chave '{chave}' existe no dicionário.")
else:
    print(f"A chave '{chave}' não existe no dicionário.")

    