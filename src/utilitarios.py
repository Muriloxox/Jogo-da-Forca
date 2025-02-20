#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli

import requests
import sqlite3
import csv

def validacao_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def voltar_ao_menu_anterior():
    while True:
        escolha = input("\n\t\tDeseja realmente voltar ao menu anterior? (S/N): ").strip().lower()
        if escolha == 's':
            return True
        elif escolha == 'n':
            return False
        else:
            print("\n\t\tOpção inválida. Digite 's' para Sim ou 'n' para Não.")

def busca_endereco(cep): 
    url_correios = 'https://viacep.com.br/ws/{CEP}/json/'

    url = url_correios.replace('{CEP}', str(cep))
    retorno_url = requests.get(url)
    dict_cep = retorno_url.json()

    endereco_completo = f'{dict_cep['logradouro']}, {dict_cep['bairro']}, {cep}, {dict_cep['localidade']}, {dict_cep['estado']}'
    return endereco_completo

def digitar_endereco():

    print('\n\t\tCEP inválido, favor digitar o endereço')

    rua = input('\n\t\tDigite a rua: ')
    bairro = input('\t\tDigite o bairro: ')
    cep = input('\t\tDigite o seu CEP: ')
    cidade = input('\t\tDigite a cidade: ')
    estado = input('\t\tDigite o estado: ')

    endereco_completo = f'{rua}, {bairro}, {cep}, {cidade}, {estado}'
    return endereco_completo

def exportar_csv():

    with sqlite3.connect('jogo_forca.db') as conecta:

        cursor = conecta.cursor()
        cursor.execute('SELECT * FROM palavras')

        with open('perguntas.csv', 'w') as arquivo:
            arquivo_csv = csv.writer(arquivo, delimiter=';')

            arquivo_csv.writerow([linha[0] for linha in cursor.description])

            for linha in cursor.fetchall():
                arquivo_csv.writerow(linha)



