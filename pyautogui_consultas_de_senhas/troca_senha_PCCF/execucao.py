import pyautogui as bot
from time import sleep
import pyperclip
import troca_imsm50
import threading
import os
import keyboard

#ambiente = ['accter imsm50']
ambiente = ['ims04']
#ambiente = ['accter cicsti']
#ambiente = ['accter cics04']

#ambiente = ['accter imsm50', 'ims04', 'accter cicsti', 'accter cics04']
#usuarios = ['I901946', 'I902046', 'I902146', 'I929446']
usuarios = ['I901946', 'I902046', 'I902146', 'I929446', 'I900746', 'I900846', 'I901046', 'I901246', 'I901346', 'I900646', 'I900146', 'I900246', 'I900946', 'I900346', 'I901146', 'I900446', 'I900546', 'I901446', 'I901546', 'I901646', 'I901746', 'i901322',
           'i935546', 'i903141', 'I906246', 'I906546', 'I906646', 'I906746', 'I907046', 'I908946', 'I909046', 'I909146', 'I909246', 'I909346', 'i924246', 'i927346', 'I903346', 'I903546', 'I903746', 'I904546', 'I905246', 'I905346', 'I905946', 'I906046']

#usuarios = ['i935546', 'i903141', 'I906246', 'I906546', 'I906646', 'I906746', 'I907046', 'I908946', 'I909046', 'I909146', 'I909246', 'I909346', 'i924246', 'i927346', 'I903346', 'I903546', 'I903746', 'I904546', 'I905246', 'I905346', 'I905946', 'I906046']

senha_atual = 'teste06'
senha_nova = 'teste07'

def iniciar():
    bot.alert('====== INICIANDO BOT DE ALTERAÇÃO DE SENHAS ======')
    sleep(1)
    bot.click('imagens/extra.png')
    sleep(1)
    bot.click(button='right')
    sleep(1)
    bot.click('imagens/renomear.png')
    sleep(1)
    bot.hotkey('ctrl', 'c')
    sleep(1)
    comparar = pyperclip.paste()
    if comparar == 'Extra':

        bot.doubleClick()
        bot.doubleClick('imagens/extra.png')
        sleep(2)
        bot.click('imagens/botao_cont.png')
        sleep(4)
        for i in ambiente:
            troca_imsm50.imsm50(i)

            if i == 'accter imsm50':
                print("")
                print('INICIANDO ALTERAÇÃO DE SENHAS NO AMBIENTE IMSM50')
                print("")
                for i in usuarios:
                    troca_imsm50.altera_senha(i, senha_atual, senha_nova)

                bot.press('f2')

            if i == 'ims04':
                print("")
                print('INICIANDO ALTERAÇÃO DE SENHAS NO AMBIENTE IMS04')
                print("")
                for i in usuarios:
                    troca_imsm50.alterar_senha_ims04(i, senha_atual, senha_nova)

                bot.press('f2')

            if i == 'accter cicsti':
                print("")
                print('INICIANDO ALTERAÇÃO DE SENHAS NO AMBIENTE CICSTI')
                print("")
                for i in usuarios:
                    troca_imsm50.alterar_senha_cicsti(i, senha_atual, senha_nova)
                bot.press('f2')

            if i == 'accter cics04':
                print("")
                print('INICIANDO ALTERAÇÃO DE SENHAS NO AMBIENTE CICS04')
                print("")
                for i in usuarios:
                    troca_imsm50.alterar_senha_cicsti(i, senha_atual, senha_nova)
                bot.press('f2')

        '''
        bot.write('accter cicsti')
        sleep(2)
        bot.press('enter')
        sleep(2)
        bot.press('f4')
        sleep(1)
        bot.write('A346005') #SENHA ATUAL TESTE11
        sleep(1)
        bot.write('teste09')
        sleep(1)
        bot.press('enter')
        sleep(1)
        bot.moveTo(631, 40)
        sleep(1)
        bot.move(663, 417)
        sleep(3)'''


    else:
        pass



    bot.alert('========= EXECUÇÃO DE BOT FINALIZADA ============')

# FUNÇÃO PARA FORÇAR INTERROMPER A EXECUÇÃO DO BOT

def parar_bot():

    while True:
        if keyboard.is_pressed('space'):
            os._exit(0)


threading.Thread(target=iniciar).start()
threading.Thread(target=parar_bot).start()