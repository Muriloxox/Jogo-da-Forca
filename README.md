# Jogo da Forca - Implementação em Python

## Descrição

Este projeto é uma implementação do clássico Jogo da Forca utilizando a linguagem Python. O jogo permite que jogadores tentem adivinhar palavras secretas com base em dicas fornecidas. Os jogadores têm um limite de tentativas e interagem com o jogo por meio de comandos de voz.

## Funcionalidades

- Cadastro de jogadores e administração via banco de dados SQLite
- Login de jogadores e administradores
- Interação por reconhecimento de voz (Speech Recognition)
- Sistema de perguntas armazenadas em banco de dados
- Recuperação de senha por e-mail
- Gerenciamento de perguntas pelo administrador

## Tecnologias Utilizadas
- Linguagem: Python
- Banco de Dados: SQLite 

## Bibliotecas:
- SpeechRecognition (reconhecimento de voz)
- pyttsx3 (conversão de texto em fala)
- requests (consulta de endereços via API do ViaCEP)
- smtplib e email (envio de e-mails)
- random (sorteio de palavras)

## Como Jogar
Execute o programa e selecione uma das opções do menu principal:
1. Jogar
- Cadastrar Novo Jogador
- Recuperar Senha
- Entrar como Administrador
- Sair

2. Caso escolha "Jogar", informe seu CPF e senha para autenticação.

3. O sistema sorteará uma palavra e exibirá a dica.

4. Fale uma letra para tentar adivinhar a palavra.

5. O jogo termina quando a palavra for descoberta ou as tentativas acabarem.

## Gerenciamento de Perguntas (Administrador)

1. O administrador pode:

- Cadastrar novas perguntas

- Atualizar perguntas existentes

- Remover perguntas

- Listar todas as perguntas e exportá-las em CSV

## Requisitos Não Funcionais

- Utilização de conceitos de Programação Orientada a Objetos (POO)

- Persistência de dados via SQLite

- Interface simples e amigável

## Observações

- Para o envio de e-mails, configure uma senha de aplicativo no Google.

- O jogo pode apresentar instabilidade no reconhecimento de voz, então fale pausadamente e próximo ao microfone.

## Contribuição Principal
<p align="center">
	
|                        **COLABORADORES**                       |                      **FUNÇÃO**                 |
| :------------------------------------------------------------- | ----------------------------------------------: |
| [**Murilo Quartezani**](https://github.com/Muriloxox)          | Programação, Documentação e Organização         |                 
| **Anna Julia Bonadiman**                                       | Programação e Organização                       |
| **Luiz Felipe Kretli**                                         | Programação e Organização                       |
</p>

## Licença

Este projeto é de uso acadêmico e não possui uma licença específica.
