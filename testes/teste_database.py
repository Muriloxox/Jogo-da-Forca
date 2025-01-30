import sqlite3

# CRIACAO DA TABELA "ADMINISTRADOR" PARA LOGIN DE USER ADMIN 
# sera que o usuario de admin tem que ser criado por interacao no programa? aqui eu fiz direto pelo banco
# definir depois quem vai ser o admin definitivo

banco = sqlite3.connect('jogo_forca.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS administrador(nome text, email text, login text, senha text)")
cursor.execute("INSERT INTO administrador VALUES('luiz felipe', 'lopeskretli922@gmail.com', 'admin', 'admin')")
cursor.execute("INSERT INTO administrador VALUES('anna julia', 'natsuya654@gmail.com', 'admin1', 'admin')")
cursor.execute("INSERT INTO administrador VALUES('murilo', 'mumurilo.2233@gmail.com', 'admin2', 'admin')")
banco.commit()

# CRIACAO DA TABELA "USUARIOS" PARA LOGIN DE USUARIOS PADRAO

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, email text, cpf text, login text, senha text)")
banco.commit()

# essa parte abaixo eu coloquei so pra exemplificar o insert e como vai pedir na main... o nome das variaveis precisam ser o mesmo das colunas

#print("Digite os dados para cadastro: ")

#nome = input('Digite seu nome: ')
#email = input('Digite seu e-mail: ')
#login = input('Digite seu login: ')
#senha = input('Digite sua senha: ')

#cursor.execute(f"INSERT INTO usuarios VALUES('{nome}', '{email}', '{cpf}', '{senha}')")
#banco.commit()

# INSERT PARA GRAVACAO DOS DADOS DIGITADOS PELO USUARIO NA TABELA "USUARIOS"

#cursor.execute(f"INSERT INTO usuarios VALUES(nome}', '{email}', '{login}', '{senha}')")
#banco.commit()

# SELECT NAS TABELAS PARA EXTRACAO DE DADOS SE NECESSARIO:

# TABELA ADMINISTRADOR

#cursor.execute("SELECT a.nome FROM administrador a WHERE a.nome = 'luiz'")
#print(cursor.fetchall())

#TABELA USUARIOS

#cursor.execute("SELECT * FROM usuarios")
#print(cursor.fetchall())
