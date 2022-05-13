import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Development\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistic = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')
print(f"{statistic.text} articles in English")

all_portals=driver.find_element(By.LINK_TEXT,"Contents")
all_portals.click()

search_wiki=driver.find_element(By.CSS_SELECTOR,'[aria-label="Search Wikipedia"]')
search_wiki.send_keys("Python")
# search_wiki.send_keys(webdriver.Keys.ENTER)
search_wiki.send_keys(Keys.ENTER)
time.sleep(3)

driver.get("http://secure-retreat-92358.herokuapp.com/")
name=driver.find_element(By.NAME,"fName")
name.send_keys("My First Name")
lname=driver.find_element(By.NAME,"lName")
lname.send_keys("My Last Name")
email=driver.find_element(By.NAME,"email")
email.send_keys("myemail@email.com")
# buton=driver.find_element(By.CSS_SELECTOR,".btn-primary")
buton=driver.find_element(By.CSS_SELECTOR,"form button")
buton.click()
time.sleep(3)
driver.quit()