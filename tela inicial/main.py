def menu():
    print("\n*** Console Retro ***")
    print("1. Bora Jogar")
    print("2. Sobre")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    return escolha

while True:
    opcao = menu()
    
    if opcao == "1":
        print("Iniciando jogo... 🎮")
    elif opcao == "2":
        print("Esse console é inspirado nos clássicos dos anos 80 e 90!")
    elif opcao == "3":
        print("Gamer das Antigas... Saindo... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")