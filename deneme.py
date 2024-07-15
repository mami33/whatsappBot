import os
import time
from my_links import *
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


app_data_dir = path.dirname(r'%APPDATA%')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument(r'--user-data-dir='+app_data_dir+'\\Local\\Google\\Chrome\\User Data')
#chrome_options.add_argument(r'--profile-directory=Profile 1')
path = os.getcwd()
ser = Service(executable_path=path + "\\chromedriver.exe", options=chrome_options)
driver = webdriver.Chrome(service=ser)

driver.get("https://web.whatsapp.com/")
time.sleep(3)

try:

    driver.find_element(By.CSS_SELECTOR, NEW_MESSAGE_BUTTON_CSS)

except NoSuchElementException:
    print("NoSuchElementException")
