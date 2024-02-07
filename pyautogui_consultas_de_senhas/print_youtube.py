import pyautogui as bot
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get('https://www.python.org')
bot.screenshot('pesquisa.png')
sleep(10)
navegador.find_element_by_id('id-search-field').send_keys('autogui', Keys.RETURN)


bot.screenshot('pesquisa.png')

'''bot.write('Jenipher lopes')
sleep(1)

bot.press('enter')
sleep(4)
img = bot.screenshot('jeniffer.png')'''


navegador.close()
bot.alert('Execução Finalizada!!!Eminem')

