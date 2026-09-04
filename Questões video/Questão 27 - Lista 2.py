#Questão 27) Uma equipe de Segurança da Informação precisa desenvolver uma
#ferramenta simples para analisar o conteúdo de arquivos de log gerados por um servidor.
#Uma das funcionalidades solicitadas é identificar a frequência com que cada letra aparece
#no arquivo. Desenvolva um programa em Python que leia um arquivo texto (.txt) e conte
#a quantidade de ocorrências de cada letra do alfabeto presente no arquivo. Para а
#contagem, considere letras maiúsculas e minúsculas como equivalentes. Espaços,
#números, sinais de pontuação e outros caracteres não devem ser contabilizados. Ao final
#do processamento, o programa deverá exibir cada letra encontrada e sua respectiva
#quantidade de ocorrências.

with open("log.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.lower()
contagem_letras = {}

for caractere in conteudo:
    if caractere.isalpha():
        if caractere in contagem_letras:
            contagem_letras[caractere] += 1
        else:
            contagem_letras[caractere] = 1

print("Frequência de letras no arquivo de log:")

for letra in contagem_letras:
    print(f"Letra:{letra} -> Ocorrências:{contagem_letras[letra]}")

