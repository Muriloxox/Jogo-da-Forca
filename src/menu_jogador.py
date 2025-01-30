import teste_jogo

def menu_jogador():

    while True:
        print(f'\n\t--------- Menu Jogo da Forca - (INSIRA NOME AQUI) --------')
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


