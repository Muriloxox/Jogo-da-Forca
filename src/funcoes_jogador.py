#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli
import sqlite3
import utilitarios
import menu_jogador
import requests

def cadastrar_jogador():

    print("\033[35m\n\t\t---------------- Cadastro para um novo jogador ----------------\n\033[0m")
    cpf = input("\t\tDigite o CPF: ")
    
    if not utilitarios.validacao_cpf(cpf):
        print("'\033[31m\n\t\tCPF inválido. Certifique-se de que tem 11 dígitos numéricos.'\033[0m")
        return

    nome = input("\t\tDigite o nome: ")
    email = input("\t\tDigite o email: ")
    senha = input("\t\tDigite a senha: ")
    cep = input('\t\tDigite seu CEP: ')

    try:
        endereco = utilitarios.busca_endereco(cep)
    except requests.exceptions.JSONDecodeError:
        cep = None

    with sqlite3.connect('jogo_forca.db') as conecta:

        cursor = conecta.cursor()
        banco = sqlite3.connect('jogo_forca.db')

        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, email text, cpf text, senha text, endereco text)")
        cursor.execute("SELECT * FROM usuarios WHERE cpf = ? AND email = ?", (cpf, email))

        if cursor.fetchone():
            print("\033[31m\n\t\tE-mail ou CPF já cadastrados.\033[0m") 
            return
        elif not email:
            print('\033[31m\n\t\tCampo nulo. Digite seu e-mail.\033[0m')  
            return 
        elif not senha:
            print('\033[31m\n\t\tCampo nulo. Digite sua senha.\033[0m')
            return
        elif not cep:
            endereco = utilitarios.digitar_endereco()
        else:
            cursor.execute('INSERT INTO usuarios (nome, email, cpf, senha, endereco) VALUES (?, ?, ?, ?, ?)', (nome, email, cpf, senha, endereco))
            banco.commit()
            print('\033[31m\n\t\tUsuário cadastrado!\033[0m')  

def checar(cpf, senha):

    with sqlite3.connect('jogo_forca.db') as conecta:
        cursor = conecta.cursor()

        login = 'SELECT * FROM usuarios WHERE cpf = ? AND senha = ?'
        cursor.execute(login, (cpf, senha))
        resultado = cursor.fetchone()
        return resultado

def login():

    print('\033[35m\n\t\t--------------- Login de Usuario ---------------\n\033[0m')
    cpf = input('\n\t\tInsira seu cpf para logar: ')
    senha = input('\t\tInsira sua senha: ')

    with sqlite3.connect('jogo_forca.db'):

        login = checar(cpf, senha)

        if login:
            menu_jogador.menu_jogador(login)
        else:
            print('\033[31m\n\t\tLogin inválido.\033[0m')
            return
        
def atualizar_dados(cpf):  
    print('\033[35m\n\t\t--------------- Alteração de dados do usuário ---------------\033[0m')

    with sqlite3.connect('jogo_forca.db') as banco:
        cursor = banco.cursor()
        cursor.execute("SELECT nome, email, senha FROM usuarios WHERE cpf = ?", (cpf,))

        print("\n\t\t1 - Alterar Nome")
        print("\t\t2 - Alterar Email")
        print("\t\t3 - Alterar Senha")
        opcao = input("\n\t\tEscolha uma opção: ")

        if opcao == '1':
            nome_novo = input("\n\t\tDigite o novo nome: ")
            cursor.execute("UPDATE usuarios SET nome = ? WHERE cpf = ?", (nome_novo, cpf))
            banco.commit()
            print("\033[31m\n\t\tCampo do nome atualizado.\033[0m")

        elif opcao == '2':
            email_novo = input("\n\t\tDigite o novo e-mail: ")
            cursor.execute("UPDATE usuarios SET email = ? WHERE cpf = ?", (email_novo, cpf))

            if cursor.fetchone():
                print("\033[31m\n\t\tEste e-mail já está em uso por outro usuário. Escolha outro e-mail.\033[0m")

            banco.commit()
            print("\033[31m\n\t\tCampo do e-mail atualizado.\033[0m")

        elif opcao == '3':
            senha_novo = input("\n\t\tDigite a nova senha: ")
            cursor.execute("UPDATE usuarios SET senha = ? WHERE cpf = ?", (senha_novo, cpf))
            banco.commit()
            print("\033[31m\n\t\tCampo da senha atualizado.\033[0m")

        else:
            print("\033[31m\n\t\tOpção inválida.\033[0m")
        
