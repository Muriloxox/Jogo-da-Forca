#anna esta passando raiva aq favor respeitar
#impressão ta uma porcaria 

from captacao_voz import ouvindo
import random
import menu_jogador

palavras = ['pipoca', 'calopsita', 'lobo']

def palavra_tracejada(palavra):
    print('\t\tPalavra: ')
    print(f' '.join(palavra))

def jogando():

    palavra_secreta = random.choice(palavras)
    palavra_atual = ['_'] * len(palavra_secreta)
    tentativas_atuais = 0
    tentativas_totais = 6

    while True:
        
        print('\n\t\t------------------ Jogo da Forca -----------------')
        print('\t\tDica: NENHUMA SE VIRA')
        print(palavra_tracejada(palavra_atual))    
        print(f'\t\tTentativas: {tentativas_atuais} / Tentativas Totais: {tentativas_totais}')

        print('\nFale uma letra: ')

        try:
            letra = ouvindo()
        except:
            print('ERRO')

        if letra[-1] in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra[-1]:
                    palavra_atual[i] = letra[-1]
            palavra_tracejada(palavra_atual)
        else:
            print('errou')
            tentativas_atuais+=1

        if tentativas_atuais > 6:
            print('GAME OVER')
            return

