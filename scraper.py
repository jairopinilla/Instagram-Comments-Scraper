from selenium import webdriver
import time
import sys
import os.path


pathcurrent = os.getcwd()
pathcurrent = pathcurrent + '\\chromedriver.exe'

driver = webdriver.Chrome(pathcurrent)

######################################
username = "rukadata"
password = "flacavonoteni30"

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
time.sleep(1)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
time.sleep(2)
driver.find_element_by_xpath("//button[contains(.,'Iniciar sesión')]").click()

time.sleep(4)
##########################################

driver.get(sys.argv[1])
time.sleep(4)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(sys.argv[2]):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)
import excel_exporter
excel_exporter.export(user_names, user_comments)

driver.close()
