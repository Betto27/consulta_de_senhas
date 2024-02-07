import pyautogui as bot
from time import sleep
import login_usuario
import pyperclip


#r = login_usuario.login('A996633')

class imsm50:

    def __init__(self, ambiente):

        sleep(3)
        self.ambiente = ambiente

        bot.write(self.ambiente)
        sleep(2)
        bot.press('enter')
        sleep(2)

        if self.ambiente == 'ims04':

            bot.press('pause')
            sleep(1)
            bot.write('/test mfs')
            bot.press('enter')
            sleep(1)
            bot.write('senhas')
            bot.press('enter')


        else:

            bot.press('f4')
            sleep(2)


class altera_senha():

    def __init__(self, usuarios, senha_atual, senha_nova):
        self.info_login = login_usuario.login(usuarios, senha_atual, senha_nova)

        bot.moveTo(780, 450)
        bot.click()
        bot.write(login_usuario.login.usuario(self.info_login))
        sleep(1)
        bot.write(login_usuario.login.senha_atual(self.info_login))
        sleep(1)
        """bot.press('tab', 3)
        sleep(2)
        bot.write(login_usuario.login.senha_nova(self.info_login))
        bot.press('tab')
        bot.write(login_usuario.login.senha_nova(self.info_login))
        sleep(1)"""
        bot.press('enter')
        #sleep(1)
        bot.press('enter')
        #sleep(1)
        bot.press('f3')
        bot.moveTo(20, 630)
        bot.click()
        sleep(1)
        # bot.click()
        bot.dragTo(700, 630, 0.5, button='left')
        #sleep(1)
        bot.click(button='right')
        #sleep(1)
        bot.moveTo(720, 415, 0.5)
        bot.click()
        info = pyperclip.paste()



        if info.strip() == '':
            print("Alteração com sucesso")
            DB2 = open('banco_imsm50.txt', 'a')
            DB2.write(f'AMBIENTE: IMSM50, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: Alteracao efetuada com sucesso. \n\n')


        else:
            print(info)
            DB2 = open('banco_imsm50.txt', 'a')
            DB2.write(f'AMBIENTE: IMSM50, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: {info}')

class alterar_senha_cicsti():

    def __init__(self, usuarios, senha_atual, senha_nova):
        self.info_login = login_usuario.login(usuarios, senha_atual, senha_nova)

        bot.moveTo(800, 450)
        bot.click()
        bot.write(login_usuario.login.usuario(self.info_login))
        #sleep(1)
        bot.write(login_usuario.login.senha_atual(self.info_login))
        #sleep(1)
        """bot.press('tab', 3)
        sleep(2)
        bot.write(login_usuario.login.senha_nova(self.info_login))
        bot.press('tab')
        bot.write(login_usuario.login.senha_nova(self.info_login))
        sleep(1)"""
        bot.press('enter')

        bot.moveTo(20, 630)
        bot.click()
        sleep(1)
        # bot.click()
        bot.dragTo(700, 630, 0.5, button='left')
        #sleep(1)
        bot.click(button='right')
        #sleep(1)
        bot.moveTo(720, 415, 0.5)
        bot.click()
        info = pyperclip.paste()

        if '7-VOLTA' in info.strip():
            print("Alteração com sucesso")
            DB2 = open('banco_cics.txt', 'a')
            DB2.write(f'AMBIENTE: CICSTI/CICS04, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: Alteracao efetuada com sucesso. \n\n')
            bot.press('f3')
            # sleep(1)
            bot.press('pause')

        elif info.strip() == "":
            print("INFORMAÇÃO NÃO FOI CAPTURADA")
            DB2 = open('banco_cics.txt', 'a')
            DB2.write(f'AMBIENTE: CICSTI/CICS04, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: INFORMAÇÃO NÃO FOI CAPTURADA')

        else:
            print(info)
            DB2 = open('banco_cics.txt', 'a')
            DB2.write(f'AMBIENTE: CICSTI/CICS04, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: {info}')



class alterar_senha_ims04():

    def __init__(self, usuarios, senha_atual, senha_nova):
        self.info_login = login_usuario.login(usuarios, senha_atual, senha_nova)

        bot.moveTo(780, 450)
        bot.click()
        bot.write(login_usuario.login.usuario(self.info_login))
        #sleep(1)
        bot.write(login_usuario.login.senha_atual(self.info_login))
        #sleep(1)
        """bot.press('tab', 3)
        sleep(2)
        bot.write(login_usuario.login.senha_nova(self.info_login))
        bot.press('tab')
        bot.write(login_usuario.login.senha_nova(self.info_login))
        sleep(1)"""
        bot.press('enter')
        #sleep(1)
        bot.press('enter')
        sleep(1)
        bot.press('f3')
        bot.moveTo(20, 630)
        bot.click()
        sleep(1)
        # bot.click()
        bot.dragTo(700, 630, 0.5, button='left')
        #sleep(1)
        bot.click(button='right')
        #sleep(1)
        bot.moveTo(720, 415, 0.5)
        bot.click()
        info = pyperclip.paste()

        if info.strip() == '':
            print("Alteração com sucesso")
            DB2 = open('banco_ims04.txt', 'a')
            DB2.write(f'AMBIENTE: IMS04, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: Alteracao efetuada com sucesso. \n\n')


        else:
            print(info)
            DB2 = open('banco_ims04.txt', 'a')
            DB2.write(f'AMBIENTE: IMS04, Usuario: {login_usuario.login.usuario(self.info_login)}, mensagem apresentada: {info}')



