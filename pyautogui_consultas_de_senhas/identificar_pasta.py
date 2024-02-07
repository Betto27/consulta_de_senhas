import pyautogui as bot
from time import sleep
import pyperclip

bot.alert('=========== Bot Iniciado !!! ===========')

bot.click('extra.png')

bot.click(button='right')
sleep(1)
bot.click('renomear.png')
sleep(1)
bot.hotkey('ctrl', 'c')
sleep(1)
comparar = pyperclip.paste()
if comparar == 'Extra':

    bot.doubleClick()
    bot.doubleClick('extra.png')
    sleep(1)
    bot.click('botao_cont.png')
    sleep(3)
    bot.write('accter cicsti')
    sleep(2)
    bot.press('enter')
    sleep(2)
    bot.press('f4')
    sleep(1)
    bot.write('A346005')
    sleep(1)
    bot.write('teste09')
    sleep(1)
    bot.press('enter')
    sleep(1)
    bot.moveTo(631, 40)
    sleep(1)
    bot.move(663, 417)
    sleep(3)


else:
    pass



bot.alert('========= Finalizado ============')