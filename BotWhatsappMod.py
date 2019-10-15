from bs4 import BeautifulSoup
from selenium import webdriver
import requests


link = 'http://web.whatsapp.com'
# driver = webdriver.Chrome()
# driver.get(link)
page = requests.get(link)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

def escuta(self):
#Vamos setar todos as mensagens no grupo.
    post = self.driver.find_elements_by_class_name('_3_7SH')
#Vamos pegar o índice da última conversa.
    ultimo = len(post) - 1
#Vamos pegar o  texto da última conversa e retornar.
    texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
    return texto







#def lerpagina(link):





# name = input('Enter the name of user or group : ')
# msg = input('Enter the message : ')
# count = int(input('Enter the count : '))
# # Scan the code before proceeding further
# input('Enter anything after scanning QR code')
# search = driver.find_element_by_class_name('_2zCfw')
# search.send_keys(name)
# driver.find_element_by_class_name('_1XCAr')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
# msg_box = driver.find_element_by_class_name('_3u328')
# for i in range(count):
#     msg_box.send_keys(msg)
#     driver.find_element_by_class_name('_3M-N-').click()
