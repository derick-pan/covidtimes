import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from time import sleep
defaultprofile = webdriver.ChromeOptions()
defaultprofile.add_argument = {
    'user-data-dir': '/Users/Application/Chrome/Default'}
driver = webdriver.Chrome(options=defaultprofile)

load_dotenv()

URL = "https://studenthealth.ucsc.edu/"

cruzid = os.getenv("CRUZID")
PASSWORD = os.getenv("PASSWORD")

driver.get(URL)

email = driver.find_element_by_id("username")
email.send_keys(cruzid)

passw = driver.find_element_by_id("password")
passw.send_keys(PASSWORD)

signin = driver.find_element_by_name("_eventId_proceed")
signin.click()

# Wait for you to fuckin do duo mobile
while (driver.current_url != "https://studenthealth.ucsc.edu/confirm.aspx"):
    sleep(1)

# Health e messenger
month = Select(driver.find_element_by_id('dtDOBMN'))
month.select_by_value('8')

# Date
date = Select(driver.find_element_by_id('dtDOBDY'))
date.select_by_value('30')

year = driver.find_element_by_id("dtDOBYR")
year.send_keys('2002')
 
signin = driver.find_element_by_name("cmdStandardProceed")
signin.click()

driver.get("https://studenthealth.ucsc.edu/Mvc/Patients/QuarantineSurvey")

# Go to the Survey Link
driver.get("https://studenthealth.ucsc.edu/CheckIn/Survey/ShowAll/15")
sleep(5)
for i in range(0, 6):
    driver.find_element_by_name(f"AllQuestions[{i}].AnswerID").click()

driver.execute_script("submitSurvey()")
driver.find_element_by_id("showQuarantineBadge").click()
