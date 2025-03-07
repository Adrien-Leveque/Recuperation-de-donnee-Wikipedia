from selenium import webdriver
from  selenium.webdriver.common.by import By
import re
import random
driver = webdriver.Chrome()
nb_p = 0

link_list = []
def extract_text(link):
    global driver, nb_p
    driver.get(url=link)
    element_list = []
    base_text = ""
    p_left = True
    i=1

    while p_left:
        try:
            element_list.append(driver.find_element(by=By.XPATH,value=("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p["+str(i)+"]")))
        except:
            p_left = False
        i+=1

    for p in element_list:
        base_text += p.text
    nb_p = i
    return base_text


def find_link():
    global driver, nb_p, link_list
    a_left = True
    a_id =1
    p_id = 2
    a_list = []
    while p_id<= nb_p:
        while a_left:
            try:
                a_list.append(driver.find_element(by=By.XPATH,value=f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[{str(p_id)}]/a[{str(a_id)}]"))
            except:
                a_left = False
            a_id+=1
        a_id =1
        a_left = True
        p_id += 1

    for a in a_list:
        link_list.append(a.get_attribute(name="href"))
    return link_list

def trans(letter, bases, goal):
    if letter in bases:
        return goal
    else:
        return letter

def go_ascii(text):
    ascii_text = ""
    ascii_regex = r"[ -~]"

    for a in text:
        a = trans(a, "éèê","e")
        a = trans(a, "àâ", "a")
        a = trans(a, "ù", "u")
        a = trans(a, "ç", "c")

        if re.match(ascii_regex, a):
            ascii_text += a
    return ascii_text

url = input("Entrer une url Wikipedia : ")
file = open("result.txt", "a")
while True:
    file.write(go_ascii(extract_text(url))+"\n")
    url = random.choice(find_link())


