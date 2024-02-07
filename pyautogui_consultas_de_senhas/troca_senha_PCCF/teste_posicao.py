import pyautogui as bot
import pyperclip
import time

bot.moveTo(20, 630)
bot.click()
time.sleep(1)
# bot.click()
bot.dragTo(700, 630, 0.5, button='left')
#time.sleep(1)
bot.click(button='right')
#time.sleep(1)
bot.moveTo(720, 415, 0.5)
bot.click()
info = pyperclip.paste()


if '7-VOLTA'in info.strip():
    print("Alteração com sucesso")

elif info.strip() == "":
    print("Informação não foi capturada")

else:
    print(info)
    print("Login")