import os
import time
from selenium import webdriver
import pyautogui

# COMPLETA ESTOS DOS CAMPOS
USERNAME = 'INGRESA TU USUARIO'
PASSWORD = 'INGRESA LA CONTRASEÑA'

def scrollDown():
        #find all li elements in list
        time.sleep(2)
        fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll <=4: # scroll 5 times
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                scroll += 1
        time.sleep(3)



def copiarNombres(lista):
    nombres = driver.find_elements_by_class_name("FPmhX")
    for i in nombres:
        nombre = i.get_attribute('href')
        if nombre not in lista:
            lista.append(nombre)


#Nombre de usuario al que se le van a scrapear los users
user = input("Nombre del user al que se le van a scrapear los seguidores:  ")

#Cantidad de usuarios que se van a scrapear
cantidad = int(input("Cantidad de usuarios que se van a scrapear:  "))
#Logear a IG y entra al perfil de un usuario
driver = webdriver.Firefox(executable_path="C:\\Users\\kkk\\Desktop\\PY-CSS\\AUTOMATIZACION\\geckodriver.exe")
driver.get("https://www.instagram.com/")
time.sleep(3)
driver.find_element_by_name("username").send_keys(USERNAME)
driver.find_element_by_name("password").send_keys(PASSWORD)
pyautogui.press("enter")
time.sleep(5)
link = "https://www.instagram.com/%s/" %user
driver.get(link)
time.sleep(1)
#click en usuarios que sigue
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)

lista = []
while len(lista) <= cantidad:
    copiarNombres(lista)
    scrollDown()

print("Lista 1 ", len(lista))

print("------------IMPRIMIENDO LA LISTA-------------------")
f = open('telefe.txt', 'w')
s1 = '\n'.join(lista)
f.write(s1)
f.close()

