from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

TWITTER_USER=os.getenv("T_USER")
TWITTER_PASS=os.getenv("T_PASS")

s=Service(r"c:\Development\chromedriver.exe")
browser=webdriver.Chrome(service=s)
browser.maximize_window()
wait=WebDriverWait(browser,30)
browser.get("https://www.twitter.com")

time.sleep(3)
giris_yap=browser.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
giris_yap.click()
username=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
username.send_keys(TWITTER_USER)
next_but=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')))
next_but.click()
passw=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
passw.send_keys(TWITTER_PASS)
login_but=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')))
login_but.click()
search=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))
search.send_keys("#100DaysOfPython")
search.send_keys(Keys.ENTER)
time.sleep(2)
last=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a')))
last.click()

countadd = 0
for i in range(0,3):
    twit=wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'[data-testid="tweet"]')))
    user=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'article .css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')))

    for item in twit:
        user_acc = user[twit.index(item)].text
        if "@" in item.text:

            print(item.text)
            print("********************************")
        else:
            print(item.text)
        countadd += 1
    htmlp=browser.find_element(By.TAG_NAME,"html")
    htmlp.send_keys(Keys.PAGE_DOWN)
print(f"Toplam: {countadd} tweet")

browser.quit()


# browser.quit()