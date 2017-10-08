#!/usr/bin/python
import telepot, time, serial, sys
ser = serial.Serial('/dev/ttyACM0', 9600)

print('Bot activado.')
print('Esperando comandos...')

def handle(msg):

        userName = msg['from']['first_name']

        content_type, chat_type, chat_id = telepot.glance(msg)

        if (content_type == 'text'):
                command = msg['text']
                print ('Comando obtenido: %s' % command)

                if  '/start' in command:
                        bot.sendMessage(chat_id, "Hola, "+userName+"\n"+"Mi nombre es: BotDuino,Te muestro la lista de comandos que puedo reconocer:"+"\n"
                                        +"/encender_led1"+" -Enciendo el Led 1"+"\n"
                                        +"/apagar_led1"+" -Apago el Led 1"+"\n"
                                        +"/encender_led2"+" -Enciendo el Led 2"+"\n"
                                        +"/apagar_led2"+" -Apago el Led 2"+"\n"
                                        +"/ubicacion"+" -Envio mi ubicacion actual"+"\n"
                                        +"/humedad"+" -Te muestro la Humedad en el ambiente"+"\n"
                                        +"/temperatura"+" -Te muestro la temperatura")

                elif '/encender' in command:
                        ser.write(b'Y')
                        bot.sendMessage(chat_id, "Led 1 Encendido!")

                elif '/apagar' in command:
                        ser.write(b'N')
                        bot.sendMessage(chat_id, "Led 1 Apagado!")

                elif '/encender_led2' in command:
                        ser.write(b'E')
                        bot.sendMessage(chat_id, "Led 2 Encendido!")

                elif '/apagar_led2' in command:
                        ser.write(b'F')
                        bot.sendMessage(chat_id, "Led 2 Apagado!")

                elif '/ubicacion' in command:
                        bot.sendLocation(chat_id, "cambiar por latitud","cambiar por longitud")

                elif '/temperatura' in command:
                        ser.write(b'T')
                        linea=ser.readline()
                        bot.sendMessage(chat_id, "Temperatura: " +linea)


                elif '/humedad' in command:
                        ser.write(b'H')
                        linea=ser.readline()
                        bot.sendMessage(chat_id, "Humedad Relativa: " +linea)
                else:
                    bot.sendMessage(chat_id, "Lo siento, no reconozco ese comando!")

TOKEN=sys.argv[1]
bot = telepot.Bot(TOKEN)

bot.message_loop(handle)

# Espera por nuevos mensajes
while 1:
        time.sleep(20)
