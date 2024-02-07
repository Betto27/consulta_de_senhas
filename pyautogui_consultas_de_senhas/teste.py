disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / 512

print(sector_amount)

'''import pyautogui as bot
from time import sleep
from selenium import webdriver
from nose.tools import assert_equal
import pyperclip
import threading
import os
import keyboard

bot.alert('Bot sendo inicializado')

def x():
    cont = 0
    while cont < 3:

        bot.moveTo(780, 450)
        bot.click()
        sleep(1)
        #bot.click()
        bot.dragTo(360, 630, 3, button='left')
        sleep(1)
        bot.click(button='right')
        sleep(1)
        bot.moveTo(380, 415, 3)
        bot.click()
        cont +=1

def y():
    while True:
        if keyboard.is_pressed('q'):
            os._exit(0)

threading.Thread(target=x).start()
threading.Thread(target=y).start()'''

'''
info = pyperclip.paste()
print(info.strip())

if info.strip() == 'PASSWORD NAO CONFERE':
    print('Password igual')
    DB2 = open('banco.txt', 'w')
    DB2.write(info)

else:
    print('Não escreveu o arquivo')'''
'''bot.moveTo(570, 70)
sleep(2)
bot.click()
sleep(1)
bot.click()
sleep(2)
bot.hotkey('ctrl', 'c')

copiado = pyperclip.paste()

sleep(1)

print(copiado)

#assert_equal(copiado, 'Evidencia das horas do mes')

if copiado == 'Evidencia das horas do mes':

    print('correto!!!!')

else:
    print('errado!!!!!!')'''