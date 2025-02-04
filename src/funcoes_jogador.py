import sqlite3
import utilitarios_futuros
import menu_jogador

def cadastrar_jogador():

    print("\n\t\tCadastro para um novo jogador")
    cpf = input("\t\tDigite o CPF: ")
    nome = input("\t\tDigite o nome: ")
    email = input("\t\tDigite o email: ")
    senha = input("\t\tDigite a senha: ")

    with sqlite3.connect('jogo_forca.db') as conecta:
        cursor = conecta.cursor()
        banco = sqlite3.connect('jogo_forca.db')

        cursor.execute()
    
        if cursor.fetchone():
            print("\n\t\tJá existe esse cpf cadastrado boyzin") 
            return
        elif not email:
            print('\n\t\tCampo nulo. Digite seu e-mail.')  
            return 
        elif not senha:
            print('\n\t\tCampo nulo. Digite sua senha.')
            return
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, email text, cpf text, login text, senha text)")
            cursor.execute('INSERT INTO usuarios (nome, email, cpf, senha) VALUES (?, ?, ?, ?)', (nome, email, cpf, senha))
            banco.commit()
            print('Usuário cadastrado!')  

def checar(cpf, senha):

    with sqlite3.connect('jogo_forca.db') as conecta:
        cursor = conecta.cursor()

        login = 'SELECT * FROM usuarios WHERE cpf = ? AND senha = ?'
        cursor.execute(login, (cpf, senha))
        resultado = cursor.fetchone()
        return resultado

def login():

    print('\n\t\tLogin de Usuario ---------------')
    cpf = input('\n\t\tInsira seu cpf para logar: ')
    senha = input('\t\tInsira sua senha: ')

    with sqlite3.connect('jogo_forca.db') as conecta:

        login = checar(cpf, senha)

        if login:
            menu_jogador.menu_jogador(login)
        else:
            print('CPF ou senha incorretos, tente novamente')
            return
        
def alterar_senha():

    print()
    
