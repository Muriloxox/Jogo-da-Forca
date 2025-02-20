#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli
import sqlite3

banco = sqlite3.connect('jogo_forca.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS administrador(nome text, email text, login text, senha text)")
cursor.execute("INSERT INTO administrador VALUES('luiz felipe', 'lopeskretli922@gmail.com', 'admin', 'admin')")
banco.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, email text, cpf text, senha text, endereco text)")
banco.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS palavras (id INTEGER PRIMARY KEY AUTOINCREMENT, dica text, palavra text, tentativas int)")
banco.commit()