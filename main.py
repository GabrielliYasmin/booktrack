meus_livros = []

while True:
    print("\n--- MENU: ---")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Atualizar leitura")
    print("4 - Avaliar livro")
    print("5 - Estatísticas")
    print("0 - Sair")

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        livro = input("Digite o nome do livro: ")
        meus_livros.append(livro)
        print(f"✔️ Livro '{livro}' adicionado com sucesso!")

    if opcao == "2":
        for livro in meus_livros:
            print(livro)

    if opcao== "0":
        print("Até logo, boa leitura! ")
        break