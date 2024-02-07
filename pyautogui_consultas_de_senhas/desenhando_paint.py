import pyautogui as bot
from time import sleep

bot.alert(' ============== BOT EM EXECUÇÂO  ==============')

bot.press('win')
sleep(1)
bot.write('word')
sleep(2)
bot.press('enter')
sleep(3)

bot.write('Vida pessoal')
sleep(1)
bot.press('enter')
sleep(1)

'''bot.moveTo(650, 350)
xOffset = 200
yOffset = 100
num_seconds = 1'''

bot.typewrite(['b', 'space', 'v', 'space', 'left', 'a', 'backspace', 'enter', 'f1'], interval=2)
#r = bot.moveRel(xOffset, yOffset, duration=num_seconds)
'''bot.drag(100, 800)
sleep(1)
bot.moveTo(650, 350)
sleep(1)
bot.moveRel(200, -600)'''


'''distance = 200

while distance > 0:
        bot.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        bot.drag(0, distance, duration=0.5)   # move down
        bot.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        bot.drag(0, -distance, duration=0.5)  # move up'''

bot.alert(' EXECUÇÂO FINALIZADA !!!')