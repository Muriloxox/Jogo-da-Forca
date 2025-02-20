#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli

import enviar_email
import menu_administrador
import funcoes_jogador

def menu():
    while True:
        print("\033[34m\n\t\tMenu Principal -----------------------\n\033[0m")
        print("\t\t1 - Jogar 🎲")
        print("\t\t2 - Cadastrar Novo Jogador 📥")
        print("\t\t3 - Recuperar Senha 📧")
        print("\t\t4 - Entrar como Administrador 💻")
        print("\t\t5 - Encerrar ❌\n")
        opcao = input("\t\tDigite sua Opção: ")

        if opcao == "1":
            funcoes_jogador.login()
        elif opcao == "2":
            funcoes_jogador.cadastrar_jogador()
        elif opcao == '3':
            enviar_email.senha()
        elif opcao == '4':
            menu_administrador.login_admin()
        elif opcao == '5':
            print("\033[31m\n\t\tSaindo do programa.\033[0m")
            break
        else:
            print("\033[31m\n\t\tOpção inválida\033[0m")

if __name__ == "__main__":
    menu()