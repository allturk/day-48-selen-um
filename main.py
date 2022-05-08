from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path=r"c:\Development\chromedriver.exe"
s=Service(executable_path=chrome_driver_path)

# driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=s)
driver.get("https://www.amazon.com.tr/Apple-%C3%A7ekirdekli-14-%C3%A7ekirdekli-GPUya-sahip-Apple-M1/dp/B09JR725DK?ref_=Oct_d_omwf_d_12601898031&pd_rd_w=5rB6v&pf_rd_p=b12ee757-72bc-41fe-a493-67b5c042e229&pf_rd_r=N9TZJZSWAVES3MD53V45&pd_rd_r=6bce771b-e5ca-411a-b70f-f29600f1290a&pd_rd_wg=lt0PO&pd_rd_i=B09JR725DK")
price=driver.find_element_by_xpath('//*[@id="attach-base-product-price"]')
print(price.get_attribute("value"))
price=driver.find_element_by_id("attach-base-product-price")

price=driver.find_element(by=By.ID,value="attach-base-product-price") #difficult to find this id,very hard
print(price.get_attribute("value"))

# driver.get("https://python.org")
# search_bar=driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

driver.get("https://python.org")
logo=driver.find_element_by_class_name("python-logo")
print(logo.size)

documentation_link=driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

xpath_submitwebsitebug=driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpath_submitwebsitebug.get_attribute("href"))

# driver.get("https://www.amazon.com.tr/Apple-%C3%A7ekirdekli-14-%C3%A7ekirdekli-GPUya-sahip-Apple-M1/dp/B09JR725DK?ref_=Oct_d_omwf_d_12601898031&pd_rd_w=5rB6v&pf_rd_p=b12ee757-72bc-41fe-a493-67b5c042e229&pf_rd_r=N9TZJZSWAVES3MD53V45&pd_rd_r=6bce771b-e5ca-411a-b70f-f29600f1290a&pd_rd_wg=lt0PO&pd_rd_i=B09JR725DK")
# price=driver.find_element_by_xpath('//*[@id="attach-base-product-price"]')
# print(price.get_attribute("value"))
# # driver.close()

driver.quit()
