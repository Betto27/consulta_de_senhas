import pyautogui
from time import sleep

pyautogui.PAUSE = 1 # Pausa a execução do autogui pelo tempo definido, utilizado como precauçao contra falhas

pyautogui.alert('======== BOT EM EXECUÇÃO ========.\n'
                'APÓS CLICAR NO BOTÃO "OK"\n'
                ' NÃO UTILIZE O MOUSE E O TECLADO DURANTE A EXECUÇÃO !!!')

r = screenWidth, screenHeight = pyautogui.size() # Pega o tamanho da tela

print(r)

y = currentMouseX, currentMouseY = pyautogui.position() # Pega a posição do cursor
print(y)

pyautogui.moveTo(130, 430) # Move o cursor para pasição definida

pyautogui.click() #Click com o botão

pyautogui.click(30, 130) #Mover o cursor e dar um click

#pyautogui.click('button.png') #Dar o click na imagem

pyautogui.move(800, -100) #Mover cursor por pixels definido
sleep(1)

pyautogui.doubleClick(60, 130) #duplo click com posiçao definida
sleep(1)

pyautogui.moveTo(500, 200, duration=2, tween=pyautogui.easeInOutQuad) #Movimentação do cursor por tempo e posiçao definida
pyautogui.click()
pyautogui.write('Hello world!', interval=0.25) #Escreve em tela e definição do intervalo de tempo para digitar cada letra
pyautogui.hotkey('ctrl', 'z') #Acionamento das teclas definidas combinadas
pyautogui.press('esc') # Acionamento da tecla ESC

with pyautogui.hold('shift'):  # Mantem pressionado uma tecla
    pyautogui.press(['right', 'right', 'right', 'right']) #Acionamento do botão direita

pyautogui.hotkey('ctrl', 'c', interval=1) #Acionamento das teclas definidas combinadas
sleep(1)



pyautogui.alert("Execução Finalizada !!!")




