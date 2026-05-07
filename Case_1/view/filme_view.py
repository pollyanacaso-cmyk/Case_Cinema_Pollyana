from controller.filme_controller import FilmeController

controller = FilmeController()

while True:

    print("\n===== SISTEMA CINEMA =====")
    print("1 - Cadastrar Filme")
    print("2 - Listar Filmes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título: ")
        genero = input("Gênero: ")
        diretor = input("Diretor: ")
        elenco = input("Elenco: ")
        duracao = int(input("Duração: "))

        controller.cadastrar(
            titulo,
            genero,
            diretor,
            elenco,
            duracao
        )

    elif opcao == "2":

        filmes = controller.listar()

        print("\n===== FILMES =====")

        for filme in filmes:
            print(f"""
ID: {filme[0]}
Título: {filme[1]}
Gênero: {filme[2]}
Diretor: {filme[3]}
Elenco: {filme[4]}
Duração: {filme[5]} min
            """)

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")