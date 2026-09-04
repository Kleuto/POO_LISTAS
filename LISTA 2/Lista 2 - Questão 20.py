def exibir_nome_do_programa():
    """Exibe o nome do sistema de forma destacada."""
    print("====================================")
    print("  SISTEMA DE GERENCIAMENTO ACADÊMICO ")
    print("====================================")

def exibir_menu():
    """Apresenta as opções disponíveis no menu para o usuário."""
    print("---=== SISTEMA ACADÊMICO ===---")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situação")
    print("0 - Sair")
    print("-------------------------------")

def cadastrar_estudante():
    """Exibe mensagem de confirmação da opção cadastrar estudante."""
    print("\nOpção Cadastrar estudante selecionada.\n")

def listar_estudantes():
    """Exibe mensagem de confirmação da opção listar estudantes."""
    print("\nOpção Listar estudantes selecionada.\n")

def alterar_situacao_estudante():
    """Exibe mensagem de confirmação da opção alterar situação."""
    print("\nOpção Alterar situação selecionada.\n")

def opcao_invalida():
    """Informa que o usuário digitou uma opção inexistente."""
    print("\nOpção inválida! Escolha uma opção do menu.\n")

def finalizar_programa():
    """Informa que o sistema está sendo fechado."""
    print("\nEncerrando o sistema... Até mais!")

def main():
    """
    Função principal que coordena o fluxo do programa.
    Controla o laço de repetição e chama as funções conforme
    a escolha do usuário.
    """
    exibir_nome_do_programa()
    
    continuar = True
    while continuar:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            alterar_situacao_estudante()
        elif opcao == "0":
            finalizar_programa()
            continuar = False  
        else:
            opcao_invalida()

main()
