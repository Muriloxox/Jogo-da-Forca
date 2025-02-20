#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli

import jogo
import funcoes_jogador
import pyttsx3
import utilitarios

def menu_jogador(jogador):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(f'Bem-vindo, {jogador[0]}')
    engine.runAndWait()

    while True:
        print(f'\033[35m\n\t\t-------------- Menu Jogo da Forca - {jogador[0]} --------------\033[0m\n')
        print('\t\t1 - Jogar 🎲')
        print('\t\t2 - Atualizar dados de cadastro 📥')
        print('\t\t3 - Voltar ao menu principal ↩️\n')
        resposta = input('\t\tSelecione uma opção: ')

        if resposta == '1':
            jogo.jogando()
        elif resposta == '2':
            funcoes_jogador.atualizar_dados(jogador[2])
        elif resposta == '3':
            if utilitarios.voltar_ao_menu_anterior():
                return
        else:
            print('\033[31m\n\t\tOpção Inválida.\033[0m')