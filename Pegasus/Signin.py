import time
import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path= '/home/bitcot/Documents/Vardhaman/PycharmProjects/Pegasus/chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.delete_all_cookies()
driver.get(config.URL)
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
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
#driver.find_element_by_xpath("//span[contains(text(),'Logout')]").click()
#time.sleep(5)
#driver.close()