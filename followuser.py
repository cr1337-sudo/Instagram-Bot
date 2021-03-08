import time
from selenium import webdriver
import random
from bs4 import BeautifulSoup as bs
import pyautogui
#Driver
driver = webdriver.Firefox(executable_path="C:\\Users\\kkk\\Desktop\\PY-CSS\\AUTOMATIZACION\\geckodriver.exe")

# complete these 2 fields ==================
USERNAME = 'massive.followers_'
PASSWORD = 'homerojs123'

driver.get("https://www.instagram.com/")
time.sleep(3)
driver.find_element_by_name("username").send_keys(USERNAME)
driver.find_element_by_name("password").send_keys(PASSWORD)
pyautogui.press("enter")
time.sleep(5)

def seguir(usuario):    
    try:

        driver.find_element_by_xpath("//*[text()='Seguir']").click()
        time.sleep(random.randint(4,7))
    except:
        pass

txt = open("telefe.txt","r")
users_50 = 0

while users_50 <= 50:
    for usuario in txt:
        driver.get(usuario)
        seguir(usuario)
        print("Siguiendo a %s" %usuario)
        users_50 += 1
        print(f"Usuarios seguidos {users_50}")
        
txt.close()