import os

restaurantes = [{"nome": "Praça", "categoria": "Comida Caseira", 'ativo': False},
                {"nome": "Pizzaria do Zé", "categoria": "Pizza", 'ativo': False},
                {"nome": "Sushi Place", "categoria": "Comida Japonesa", 'ativo': False}]

def limpar_tela() -> None:
    '''
    Limpa a tela do terminal.
    '''
    os.system("cls" if os.name == "nt" else "clear")

def exibir_nome_do_programa() -> None:
    '''
    Exibe o nome do programa 'Sabor Express' em arte ASCII.
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes() -> None:
    '''
    Exibe as opções do menu principal.
    '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def pausar() -> None:
    '''
    Pausa a execução do programa até que o usuário pressione qualquer tecla.
    '''
    input("\nPressione ENTER para continuar...")

def finalizar_app() -> None:
    '''
    Finaliza a aplicação, limpa a tela e exibe uma mensagem de despedida.
    '''
    limpar_tela()
    print("Finalizando aplicação... Até mais!")
    return

def escolher_opcao() -> int:
    '''
    Solicita ao usuário que escolha uma opção do menu e retorna a opção escolhida.
    '''
    while True:
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número (1 a 4).")

def cadastrar_restaurante() -> None:
    '''
    Cadastra um novo restaurante solicitando nome e categoria ao usuário.

    Inputs:
    - nome_do_restaurante: Nome do restaurante a ser cadastrado.
    - categoria_restaurante: Categoria do restaurante a ser cadastrado.

    Outputs:
    - Adiciona um dicionário com os dados do restaurante à lista 'restaurantes'.
    '''
    print("Cadastrando restaurante...")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite a categoria do {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_restaurante}
    restaurantes.append(dados_do_restaurante)
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso!")
    input("Pressione ENTER para voltar o menu principal...")
    main()

def listar_restaurantes() -> None:
    '''
    Lista todos os restaurantes cadastrados, contendo nome, categoria e estado e se estão ativos ou inativos.

    Outputs:
    - Exibe uma lista formatada de restaurantes com seus respectivos dados.
    '''
    print("Listando restaurantes...")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for idx, restaurante in enumerate(restaurantes, start=1):
            print(f"{idx}. {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(15)} | {'Ativo' if restaurante.get('ativo', False) else 'Inativo'}")
    input("\nPressione ENTER para voltar o menu principal...")
    main()

def alternar_estado_restaurante() -> None:
    '''
    Alterna o estado de um restaurante entre ativo e inativo com base no nome fornecido pelo usuário.
    
    Outputs:
    - Atualiza o estado do restaurante na lista 'restaurantes' e exibe uma mensagem de confirmação.
    
    '''
    print("Alternando estado do restaurante...")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante.get('ativo', False)
            estado = "ativado" if restaurante['ativo'] else "desativado"
            print(f"Restaurante '{nome_restaurante}' foi {estado}.")
            break
    if not restaurante_encontrado:
        print(f"Restaurante '{nome_restaurante}' não encontrado.")
    pausar()

def main() -> None:
    '''
    Função principal que executa o loop do menu do programa.

    Outputs:
    - Executa as funções correspondentes às opções escolhidas pelo usuário.
    '''
    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes()

        opcao = escolher_opcao()

        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")
            pausar()

if __name__ == "__main__":
    main()
