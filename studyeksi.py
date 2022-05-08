from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import time
s=Service(r"C:\Development\chromedriver.exe")
browser=webdriver.Chrome(service=s)
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pagecount=1
entries=[]
entrycount=1
while pagecount<=10:
    randomPage=random.randint(1,1290)
    newurl=url+str(randomPage)
    browser.get(newurl)
    time.sleep(3)
    elements=browser.find_elements(By.CSS_SELECTOR,value=".content")
    for element in elements:
        entries.append(element.text)
    pagecount+=1

with open("entries.txt","w",encoding="utf-8") as file:
    for entry in entries:
        file.write(str(entrycount)+".\n"+entry+"\n")
        file.write("********************************\n")
        entrycount+=1

browser.quit()