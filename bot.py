#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial , sys , time
ser = serial.Serial('/dev/ttyACM0' , 9600)
# Importamos las librerías necesarias
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

from random import getrandbits
# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=mensaje)
    print("ID: " + str(id) + " MENSAJE: " + mensaje)
    #
    if mensaje=="ola" :  #sanalizamos el mensaje que nos ha llegado
        bot.sendMessage(chat_id=update.message.chat_id, text='tonto')
        #la idea seria entonces abrir el puesto y que se comuniquen losel arduino y yo, asi poder enciar ordenes a mi arduino
    elif mensaje=="vaya mierda":
        bot.sendMessage(chat_id=update.message.chat_id, text='tu si que eres una mierda')
# Método que utilizaremos para cuando se mande el comando de "start"
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Bienvenido al bot de Bytelix!')
    # Aqui podriamo inicializar un juego, como se inicia un juego?

# Método que mandará el mensaje "¡Hola, lector de Bytelix!"
def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola, lector de Bytelix!')

# Método que mandará el logo de la página
def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendMessage(chat_id=update.message.chat_id, text='¡en teoria enviamos una foto!')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('prueba.png', 'rb'))

def encender(bot,update):
    ser.write(b'Y')
    bot.sendMessage(chat_id=update.message.chat_id, text='¡encendemos el led!')
    bot.sendMessage(chat_id=update.message.chat_id, text='https://google.com')
def apagar(bot,update):
    ser.write(b'N')
    bot.sendMessage(chat_id=update.message.chat_id, text='¡apagamos el led!')
def value_ardu(bot,update):
    ser.write(b'H')
    valor=ser.readline()
    bot.sendMessage(chat_id=update.message.chat_id, text='respuesta del arduino '+valor)
def inline(bot, update):
    # Sólo procesaremos el inline cuando haya algún texto introducido
    query = update.inline_query.query

    if not query:
        return

    texto_inline = query
    resultados = list()

    # Texto que se enviará y se mostrará al usuario
    alternativa1_texto = 'Hola desde el bot de Bytelix, ' + texto_inline
    alternativa2_texto = 'Bienvenido, ' + texto_inline
    alternativa3_texto = '¿Conoces Bytelix, ' + texto_inline + '?'

    # Resultados que se mostrarán para elegir
    alternativa1 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa1_texto,
        input_message_content=InputTextMessageContent(alternativa1_texto))

    alternativa2 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa2_texto,
        input_message_content=InputTextMessageContent(alternativa2_texto))

    alternativa3 = InlineQueryResultArticle(
        id=hex(getrandbits(64))[2:],
        title=alternativa3_texto,
        input_message_content=InputTextMessageContent(alternativa3_texto))

    # Añadimos los resultados que hemos creado a la lista de resultados
    resultados.append(alternativa1)
    resultados.append(alternativa2)
    resultados.append(alternativa3)

    # Y mostramos la lista al usuario
    bot.answerInlineQuery(update.inline_query.id, results=resultados)

def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    # Por supuesto no os olvidéis de cambiar donde pone "TOKEN" por el token que os ha dado BotFather
    updater = Updater(TOKEN)

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    # Ahora registramos cada método a los comandos necesarios
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holamundo", hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", logo))
    dispatcher.add_handler(CommandHandler("encender", encender))
    dispatcher.add_handler(CommandHandler("apagar", apagar))
    dispatcher.add_handler(CommandHandler("valor", value_ardu))

    dispatcher.add_handler(InlineQueryHandler(inline))

    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()

# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    TOKEN=sys.argv[1]
    if TOKEN :
        print "inicio bot"
        main()
    else:
        print "Error no puedes entrar"
