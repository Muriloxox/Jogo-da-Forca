import teste_jogo
import funcoes_jogador
import pyttsx3

def menu_jogador(jogador):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(f'Bem-vindo, {jogador[0]}')
    engine.runAndWait()

    while True:
        print(f'\n\t\tMenu Jogo da Forca - {jogador[0]} --------------')
        print('\t\t1 - Jogar')
        print('\t\t2 - Atualizar Dados')
        print('\t\t3 - Voltar ao Menu Principal')
        resposta = input('\t\tSelecione uma opção: ')

        if resposta == '1':
            teste_jogo.jogando()
        elif resposta == '2':
            print
        elif resposta == '3':
            return


