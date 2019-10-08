
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

# Scan the code before proceeding further
input('Enter anything after scanning QR code')



search = driver.find_element_by_class_name('_2zCfw')
search.send_keys(name)
driver.find_element_by_class_name('_1XCAr')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()
