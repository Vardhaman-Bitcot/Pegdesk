import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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
driver.find_element_by_xpath("//i[@class='fa fa-plus icn_plus']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@name='account[name]']").send_keys("Bitcot")
driver.find_element_by_xpath("//input[@name='account[account_number]']").send_keys("Technology")
driver.find_element_by_xpath("//input[@id='googleAddress']").send_keys("92127")
time.sleep(2)
driver.find_element_by_xpath("//div[@class='autocomplete-dropdown-container']//div[1]").click()
time.sleep(2)
Selector = Select(driver.find_element_by_name("account[region_id]"))
Selector.select_by_index(10)
time.sleep(2)
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





