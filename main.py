import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import time
driver = webdriver.Chrome()
load_dotenv()

URL = "https://studenthealth.ucsc.edu/"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def site_login():
    driver.get(URL)


class EmessengerLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install())
        self.driver.get(URL)
        time.sleep(1)  # Wait for some time to load
        print(EMAIL)
        print(PASSWORD)

    def login(self):
        email = self.driver.find_element_by_id("email")
        email.send_keys(self.email)

        password = self.driver.find_element_by_id("pass")
        password.send_keys(self.password)

        self.driver.find_element_by_id("loginbutton").click()


if __name__ == '__main__':
    # Enter your login credentials here
    UCSClogin = EmessengerLogin(
        email=EMAIL, password=PASSWORD, browser='Chrome')
    UCSClogin.login()
    driver.quit()
