from selenium import webdriver
from  selenium.webdriver.common.by import By
import re
import random
import unicodedata
driver = webdriver.Chrome()
nb_p = 0

url_list = []
def extract_text(url):
    global driver, nb_p
    driver.get(url=url)
    p_list = [element for element in driver.find_elements(by=By.CSS_SELECTOR,value="#mw-content-text > div.mw-content-ltr.mw-parser-output > p:")]
    text = ""


    for p in p_list:
        text += p.text
    return text


def find_link():
    global driver,  url_list

    a_list = [link for link in driver.find_elements(by=By.CSS_SELECTOR,value="#mw-content-text > div.mw-content-ltr.mw-parser-output > p > a:")]


    for a in a_list:
        url_list.append(a.get_attribute(name="href"))
    return url_list



def go_ascii(text):
    normalized = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join(c for c in normalized if ord(c) < 128)
    return ascii_text

url = "https://fr.wikipedia.org/wiki/Mathématiques"
file = open("result.txt", "a")
while True:
    file.write(go_ascii(extract_text(url)))
    url = random.choice(find_link())


