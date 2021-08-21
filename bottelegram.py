#instalado PyTelegrambotpi para conectar ao Telegram, importar telebot
#antes buscar BotFather no telegram para criar bot e obter chave API

import telebot
#
chave_api = "1982243772:AAGYqTOXqgMs46tNbdYDlsGU_VU3U1K_AWE"

#comando abaixo faz a conexão com Telegram atraves da chave_api
bot = telebot.TeleBot(chave_api)

#Guarda variaveis, facilita o trabalho
face = "https://www.facebook.com/brasilciclismo.com.br"
site = "http://brasilciclismo.com.br"
twitter = "https://twitter.com/Ciclismo_Br"

#sempre necessa´rio comando @bot.message_handler para habilitar opção!

@bot.message_handler(commands=["opcao1"])
def opcao1 (mensagem):
    print(mensagem)
    bot.send_message((mensagem.chat.id), face)

@bot.message_handler(commands=["opcao2"])
def opcao1 (mensagem):
    print(mensagem)
    bot.send_message((mensagem.chat.id), site)

@bot.message_handler(commands=["opcao3"])
def opcao1 (mensagem):
    print(mensagem)
    bot.send_message((mensagem.chat.id),twitter)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para proseguir (Clique na opção)
    /opcao1 - Ir para o Facebook
    /opcao2 - Ir para o site!
    /opcao3 - Ir para o Twiter
    Somenbte as opções acima são válidas!!"""
    bot.reply_to(mensagem, texto)
#para listar necessário /opçao (estudando ainda outra forma!
bot.polling()

