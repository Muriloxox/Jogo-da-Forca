# murilo esteve aqui 🐦🔥
#anna passou aqui 🥵👻
import requests

#validar cpf
def validacao_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

#formatar palavra no jogo e na mensagem
def formatacao_palavra(palavra, letras_certas):
    return " ".join([letra if letra in letras_certas else "_" for letra in palavra])

#centralizar uma msg, tlg?
def exibir_mensagem_centralizada_bonito_com_tracos_em_cima(mensagem):
    print("\n" + "-" * len(mensagem))
    print(mensagem)
    print("-" * len(mensagem))

#funcao pra voltar no menu anterior
def voltar_menu(funcao_menu):
    while True:
        funcao_menu()
        opcao = input("Voltar ao menu anterior? ")
        opcao.lower()
        if opcao == 'sim' or 's' or 'si':
            break

#funcao pra buscar o cep e adiantar algo futuro
def busca_endereco(cep):
    url_correios = 'https://viacep.com.br/ws/{CEP}/json/'

    url = url_correios.replace('{CEP}', str(cep))
    retorno_url = requests.get(url)
    dict_cep = retorno_url.json()

    endereco_completo = f'{dict_cep['logradouro']}, {dict_cep['bairro']}, {cep}, {dict_cep['localidade']}, {dict_cep['estado']}'
    return endereco_completo

def digitar_endereco():
    rua = input('\n\t\tDigite a rua: ')
    bairro = input('\t\tDigite o bairro: ')
    cep = input('\t\tDigite o seu CEP: ')
    cidade = input('\t\tDigite a cidade: ')
    estado = input('\t\tDigite o estado: ')

    endereco_completo = f'{rua}, {bairro}, {cep}, {cidade}, {estado}'
    return endereco_completo
