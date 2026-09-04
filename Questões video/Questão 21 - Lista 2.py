#Questão 21) Um estudante do IF Baiano está organizando sua rotina de estudos para a
#semana. Ele pretende dedicar um determinado número de horas para estudar
#Programação, Banco de Dados e Redes de Computadores.
#Desenvolva um programa que receba a quantidade de horas de estudo para cada uma das
#três disciplinas e exiba a carga horária total planejada.
#Entretanto, caso alguma das horas informadas seja negativa, o programa deverá informar
#que os valores são inválidos e não realizar o cálculo da carga horária total.
#Entrada
# Horas de estudo para Programação.
# Horas de estudo para Banco de Dados.
# Horas de estudo para Redes de Computadores.

horas_programacao = float(input("Digite o número de horas de Programação:"))
horas_bd = float(input("Digite o número de horas de Banco de Dados:"))
horas_redes = float(input("Digite o número de horas de Redes de Computadores:"))

if horas_programacao < 0 or horas_bd < 0 or horas_redes < 0:
    print("Valores são invalidos! Digite números positivos.")
else:
    horas_total = horas_programacao + horas_bd + horas_redes
    print(f"Carga horária total planejada:{horas_total:.2f} horas")

    