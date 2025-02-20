#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli

import sqlite3
import utilitarios

def login_admin():

    print('\033[31m\n\t\t--------------- Login de ADM ---------------\n\033[0m')
    cpf = input('\t\tInsira seu login: ')
    senha = input('\t\tInsira sua senha: ')    

    with sqlite3.connect('jogo_forca.db'):

        login = checar(cpf, senha)

        if login:
            menu_adm(login)
        else:
            print('\033[31m\n\t\tLogin inválido.\033[0m')
            return
    
def checar(login, senha):

    with sqlite3.connect('jogo_forca.db') as banco:
        cursor = banco.cursor()

        entrar = 'SELECT * FROM administrador WHERE login = ? AND senha = ?'
        cursor.execute(entrar, (login, senha))
        resultado = cursor.fetchone()
        return resultado

def cadastrar_palavra():

    palavra = input("\n\t\tDigite a palavra: ")
    dica = input('\t\tDigite a dica da palavra: ')
    tentativas = int(input('\t\tDigite a quantidade máxima de tentativas: '))

    with sqlite3.connect('jogo_forca.db') as banco:

        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS palavras (id INTEGER PRIMARY KEY AUTOINCREMENT, dica text, palavra text, tentativas int)")
        cursor.execute("INSERT INTO palavras (dica, palavra, tentativas) VALUES (?, ?, ?)", (dica, palavra, tentativas))
        banco.commit()

    print("\033[31m\n\t\tPalavra cadastrada.\033[0m")

def listar_palavras():

    with sqlite3.connect('jogo_forca.db') as banco:

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM palavras")
        resultado = cursor.fetchall()

        print('\n\t\t  código    dica   palavra   tentativas')

        for i in resultado:
            print('\n\t\t', i)

    print('\n\t\tDeseja exportar os dados das perguntas em CSV?')
    resposta = input('\t\t(S/N): ')

    if resposta == 'S' or resposta == 's':
        utilitarios.exportar_csv()
    else:
        return

def atualizar_palavra():

    listar_palavras() 
    
    id_palavra = input("\n\t\tDigite o ID da palavra que deseja atualizar: ")
    nova_palavra = input("\t\tDigite a nova palavra: ")

    with sqlite3.connect('jogo_forca.db') as banco:

        cursor = banco.cursor()
        cursor.execute("UPDATE palavras SET palavra = ? WHERE id = ?", (nova_palavra, id_palavra))
        banco.commit()

    print("\033[31m\n\t\tPalavra alterada.\033[0m")

def remover_palavra():

    listar_palavras()  
    
    id_palavra = input("\n\t\tDigite o ID da palavra que deseja remover: ")

    with sqlite3.connect('jogo_forca.db') as banco:
        cursor = banco.cursor()
        cursor.execute("DELETE FROM palavras WHERE id = ?", (id_palavra,))
        banco.commit()

    print("\033[31m\n\t\tPalavra removida.\033[0m")  

def menu_adm(login):

    while True:
        print(f"\033[31m\n\t\t-------------- Menu Administrador ------ {login[0]} -------\n\033[0m")
        print("\t\t1 - Cadastrar nova palavra 🧩")
        print("\t\t2 - Atualizar palavra ✏️")
        print("\t\t3 - Remover palavra ✂️")
        print("\t\t4 - Listar palavras 🎯")
        print("\t\t5 - Voltar menu principal  ↩️\n")
        opcao = input("\t\tDigite a opção: ")
    
        if opcao == '1':
            cadastrar_palavra()
        elif opcao == '2':
            atualizar_palavra()
        elif opcao == '3':
            remover_palavra()
        elif opcao == '4':
            listar_palavras()
        elif opcao == '5':
            if utilitarios.voltar_ao_menu_anterior():
                return