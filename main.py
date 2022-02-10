import os
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
# import time
from time import sleep

driver = webdriver.Chrome()
load_dotenv()

URL = "https://studenthealth.ucsc.edu/"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver.get(URL)


email = driver.find_element_by_id("username")
email.send_keys(EMAIL)


passw = driver.find_element_by_id("password")
passw.send_keys(PASSWORD)


signin = driver.find_element_by_name("_eventId_proceed")
signin.click()

sleep(100)  # Wait for you to fuckin do duo mobile


# driver.quit()
