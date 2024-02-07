import pyautogui as bot
from time import sleep

bot.alert('Bot Iniciado')

cont = 0
while cont < 4:

    cont += 1
    bot.moveTo(100, 90)
    bot.click(button="right")
    sleep(1)
    bot.moveTo(140, 330)
    bot.click()
    sleep(1)
    bot.press('enter')

bot.alert('Bot Finalizado!!!')