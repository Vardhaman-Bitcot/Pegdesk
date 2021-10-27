import time

from selenium.webdriver.support import select
import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_page_load_timeout(200)
driver.maximize_window()
driver.delete_all_cookies()
driver.get(config.URL)
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1. Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys(config.Email_id)
driver.find_element_by_name("user[password]").send_keys(config.PassWord)
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
time.sleep(10)
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

#Validating the account
print("2.Check whether superadmin is able to create account successfully")
driver.find_element_by_link_text("Jobs").click()
time.sleep(5)
driver.find_element_by_xpath("//i[@class='fa fa-plus icn_plus']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@name='account[name]']").send_keys(config.Account_name)
driver.find_element_by_xpath("//input[@name='account[account_number]']").send_keys(config.Account_number)
driver.find_element_by_xpath("//input[@id='googleAddress']").send_keys(config.Street_address)
time.sleep(2)
driver.find_element_by_xpath("//div[@class='autocomplete-dropdown-container']//div[1]").click()
time.sleep(2)
Region = Select(driver.find_element_by_name("account[region_id]"))
Region.select_by_index(10)
time.sleep(2)
Timezone = Select(driver.find_element_by_xpath("xpath=//select[@name='account[timezone]']"))
Timezone.select_by_index(8)
time.sleep(3)
Company = Select(driver.find_element_by_xpath("xpath=//select[@name='account[company_account_id]']"))
Company.select_by_index(3)
time.sleep(3)
submit = driver.find_element_by_xpath("(//button)[contains(text(),'Submit')]").click()
time.sleep(2)
found = False
while not found:
        try:
            ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Go')]")))
            found = True
            print("Account created successfully")
        except (NoSuchElementException, TimeoutException) as e:
            time.sleep(2)
            print("Unable to create the account:", 'Account Number has already been taken')
            driver.quit()
            exit()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(.,'Go')]").click()
driver.quit()





