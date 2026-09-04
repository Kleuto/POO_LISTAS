estudantes = {
    "Kaike": {
        "nota1": 8.0,
        "nota2": 7.0,
        "media": 7.5
    },

    "Diogo": {
        "nota1": 9.0,
        "nota2": 6.0,
        "media": 7.5
    },

    "Higor": {
        "nota1": 5.0,
        "nota2": 6.0,
        "media": 5.5
    }
}

for nome, dados in estudantes.items():

    if dados["media"] >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Aluno:", nome)
    print("Nota 1:", dados["nota1"])
    print("Nota 2:", dados["nota2"])
    print("Média:", dados["media"])
    print("Situação:", situacao)
    print()