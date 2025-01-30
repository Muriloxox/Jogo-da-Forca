# murilo esteve aqui 🐦🔥
import enviar_email
import menu_adm
import funcoes_jogador

def menu():
    while True:
        print("\n\t\tMenu Principal -----------------------")
        print("\t\t1 - Jogar 🎲")
        print("\t\t2 - Cadastrar Novo Jogador 📥")
        print("\t\t3 - Recuperar Senha 📧")
        print("\t\t4 - Entrar como Administrador 💻")
        print("\t\t5 - Sair ❌")
        opcao = input("\t\tDigite a opção desejada: ")

        if opcao == "1":
            funcoes_jogador.login()
        elif opcao == "2":
            funcoes_jogador.cadastrar_jogador()
        elif opcao == '3':
            enviar_email.senha()
        elif opcao == '4':
            menu_adm()
        elif opcao == '5':
            print("\n\t\tSaindo do programa.")
            break
        else:
            print("\n\t\tOpção inválida")

if __name__ == "__main__":
    menu()