import os

restaurantes = []

def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def exibir_nome_do_programa() -> None:
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes() -> None:
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def pausar() -> None:
    input("\nPressione ENTER para continuar...")

def finalizar_app() -> None:
    limpar_tela()
    print("Finalizando aplicação... Até mais!")
    return

def escolher_opcao() -> int:
    while True:
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número (1 a 4).")

def cadastrar_restaurante() -> None:
    print("Cadastrando restaurante...")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso!")
    input("Pressione ENTER para voltar o menu principal...")
    main()

def listar_restaurantes() -> None:
    print("Listando restaurantes...")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for idx, restaurante in enumerate(restaurantes, start=1):
            print(f"{idx}. {restaurante}")
    input("\nPressione ENTER para voltar o menu principal...")
    main()

def ativar_restaurante() -> None:
    print("Ativando restaurante...")
    pausar()

def main() -> None:
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
            ativar_restaurante()
        elif opcao == 4:
            finalizar_app()
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")
            pausar()

if __name__ == "__main__":
    main()
