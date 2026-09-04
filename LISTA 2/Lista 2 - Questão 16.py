estudantes = {
    "Kaike": 8.0,
    "Gabriel": 7.0,
    "Higor": 6.0,
    "David": 5.0
}

for nome, nota in estudantes.items():

    if nota >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Nome:", nome)
    print("Nota:", nota)
    print("Situação:", situacao)
    print()