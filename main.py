meus_livros = []

while True:
    print("\n--- MENU: ---")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Atualizar leitura")
    print("4 - Avaliar livro")
    print("5 - Estatísticas")
    print("6 - Resetar lista")  # Temporário
    print("0 - Sair")

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        livro = input("Digite o nome do livro: ")
        meus_livros.append({"nome": livro, "status": "Não iniciado"})
        print(f"✔️ Livro '{livro}' adicionado com sucesso!")

    elif opcao == "2":
        print("\n--- SUA LISTA DE LIVROS ---")

        if len(meus_livros) == 0:
            print("Nenhum livro cadastrado ainda.")
        else:
            for i, livro in enumerate(meus_livros, start=1):
                print(f"{i} - {livro['nome']} | Status: {livro['status']}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":
        print("\n--- ESCOLHA O LIVRO ---")

        for i, livro in enumerate(meus_livros, start=1):
            print(f"{i} - {livro['nome']}")

        escolha = int(input("Escolha o número do livro: "))

        livro = meus_livros[escolha - 1]

        print(f"\nLivro selecionado: {livro['nome']}")

        print("\nEscolha o novo status:")
        print("1 - Não iniciado")
        print("2 - Lendo")
        print("3 - Finalizado")

        status = input("Escolha o status: ")

        if status == "1":
            livro["status"] = "Não iniciado"
        elif status == "2":
            livro["status"] = "Lendo"
        elif status == "3":
            livro["status"] = "Finalizado"

        print("Leitura atualizada com sucesso! ✔️")

    elif opcao == "4":
        print("\n--- ESCOLHA O LIVRO ---")

        for i, livro in enumerate(meus_livros, start=1):
            print(f"{i} - {livro['nome']}")

        escolha = int(input("Escolha o número do livro: "))

        livro = meus_livros[escolha - 1]

        print(f"\nLivro selecionado: {livro['nome']}")

        nota = input("Qual foi a sua nota final para o livro? ")

        livro["avaliacao"] = nota

        print("Livro avaliado com sucesso! ✔️")

    elif opcao == "5":
        total_livros = len(meus_livros)
        print("\n--- Estatísticas ---")
        print(f"Total de livros cadastrados: {total_livros}")

    elif opcao == "6":
        meus_livros.clear()
        print("Todos os livros foram apagados! Lista resetada com sucesso!")

    elif opcao == "0":
        print("Até logo, boa leitura!")
        break
