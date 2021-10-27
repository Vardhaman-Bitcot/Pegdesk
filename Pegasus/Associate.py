import time
import config
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_page_load_timeout(200)
driver.maximize_window()
driver.delete_all_cookies()
driver.get(config.URL)
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
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
print("2.Check whether superadmin able to associate with this account")
driver.find_element_by_xpath("//span[contains(.,'Accounts')]").click()
ex_wait.until(EC.element_to_be_clickable((By.XPATH , "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Associate User')]").click()
time.sleep(5)
actions = ActionChains(driver)
answer=actions.send_keys(Keys.TAB,Keys.TAB,"testqa@bitcot.com",Keys.TAB)
actions.perform()
time.sleep(3)
if answer == 'testqa+test@bitcot.com':
    print("Email Id is matching")
else:
    print("email is not match")
    driver.quit()
    exit()
driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
time.sleep(5)
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
driver.quit()