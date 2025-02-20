#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli

from captacao_voz import ouvindo
import random
import sqlite3

def gerar_palavra():

    with sqlite3.connect('jogo_forca.db') as banco:

        cursor = banco.cursor()
        teste = ('SELECT * FROM palavras')
        cursor.execute(teste)
        resultado = cursor.fetchall()

        if resultado:
            palavra_aleatoria = random.choice(resultado)
            return palavra_aleatoria
        else:
            print('\033[31m\n\t\tNenhuma palavra cadastrada!\033[0m')
            return

def validar_letra(fala):

    if fala[0]  == 'letra' and len(fala) == 2:
        return fala[1]
    else:
        return None

def palavra_tracejada(palavra):

    return ' '.join(palavra)

def jogando():

    palavra = gerar_palavra()
    palavra_tabela = palavra[2]
    palavra_secreta = str(palavra[2].lower())
    
    palavra_atual = []

    for letra in palavra_secreta:
        if letra == ' ':
            palavra_atual.append(' ')
        else:
            palavra_atual.append('_')

    tentativas_atuais = 0

    while True:
        
        print('\033[35m\n\t\t------------------ Jogo da Forca -----------------\n\033[0m')
        print(f'\t\tDica: {palavra[1]}')
        print('\t\tPalavra: ', palavra_tracejada(palavra_atual))    
        print(f'\t\tTentativas:  {tentativas_atuais} / Tentativas Totais: {palavra[3]}')

        print('\n\t\tFale uma letra: ')

        texto = ouvindo()

        if texto:
            letra = validar_letra(texto)

            if letra == None:
                print('\n\t\tLetra não reconhecida, tente novamente!')
            else: 
                if letra.lower() in palavra_secreta:
                    for i in range(len(palavra_secreta)):
                        if palavra_secreta[i] == letra.lower():
                            palavra_atual[i] = palavra_tabela[i]
                else:
                    print(f'\n\t\tLetra {letra} não está na palavra!')
                    tentativas_atuais+=1
        else:
            print('\n\t\tLetra não reconhecida, tente novamente!')

        if '_' not in palavra_atual:
            print(f'\n\t\tParabéns, a palavra era {palavra[2]}!')
            return

        if tentativas_atuais == palavra[3]:
            print(f'\n\t\tGAME OVER! A palavra era {palavra[2]}! ☠️')
            return

