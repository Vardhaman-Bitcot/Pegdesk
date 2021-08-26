import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def send_keys_delayed(elementName, str):
   for char in str:
      driver.find_element_by_name(elementName).send_keys(char)
      time.sleep(random.uniform(0.03,0.2))

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://qa.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 30)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
found = False
while not found:
    try:
        Account_wait = ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT , "Quotes")))
        found = True
        print("Login success")
    except (NoSuchElementException,TimeoutException) as e:
        time.sleep(2)
        print("Login error")
        driver.quit()
        exit()
time.sleep(3)
print("2.Check whether able to create frontline user")
ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT , "Frontline Users"))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH ,"//button[@class='float-right btn btn-secondary cst_btn mr-1 mb-1 min-width-btn']"))).click()
driver.find_element_by_xpath("//input[@id='first_name']").send_keys("Qwerty")
driver.find_element_by_xpath("//input[@id='last_name']").send_keys("Keyboard")
driver.find_element_by_xpath("//div[4]//input[1]").send_keys("1000001")
send_keys_delayed("frontline[dob_password]","1010")
driver.find_element_by_name("frontline[dob_password]").send_keys(Keys.TAB,"Bitcot",Keys.ARROW_UP,Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("//button[@class='btn cst_btn btn_danger mr-2']").click()
driver.save_screenshot('FU.png')
found = False
while not found:
        try:
            ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Import CSV')]")))
            found = True
            print("Frontline user is created successfully")
        except (NoSuchElementException, TimeoutException) as e:
            time.sleep(2)
            print("Unable to create frontline user:", 'Employee ID has already been taken')
            driver.quit()
            exit()

time.sleep(3)
driver.find_element_by_xpath("//button[contains(.,'Import CSV')]").click()
driver.close()
