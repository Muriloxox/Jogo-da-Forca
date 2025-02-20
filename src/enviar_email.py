#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def enviar_email (destinatario, assunto, mensagem):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = 'natsuya654@gmail.com'
    senha = ''

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain')) 

    try:
        #conexao com o server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, senha)

        server.sendmail(remetente, destinatario, msg.as_string())
        print('\n\t\tE-mail enviado com sucesso')

    except Exception as e:
        print(f'\n\t\tFalha ao enviar email: {e}')

    finally:
        server.quit()

def senha():
    escolhas = ['!', '@', '#', '$']
    senha = ''

    for i in range(5):
        senha += random.choice(escolhas)

    email_jogador = input('\n\t\tDigite o e-mail cadastrado: ')

    with sqlite3.connect('jogo_forca.db') as conecta:
        cursor = conecta.cursor()
        
        email = checar_email(email_jogador)

        if email:
            cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (senha, email_jogador))
            enviar_email(email_jogador, 'Recuperação Senha', f'Oi, {email[0]}\nsua nova senha é {senha}') 
        else:
            print('\n\t\tE-mail não cadastrado no sistema, tente novamente')

def checar_email(email):

      with sqlite3.connect('jogo_forca.db') as conecta:
        cursor = conecta.cursor()
        
        login = 'SELECT * FROM usuarios WHERE email = ?'
        cursor.execute(login, [email])

        resultado = cursor.fetchone()
        return resultado