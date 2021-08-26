import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://qa.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 30)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
print("Login successfully")
print("2.Check whether able to import CSV frontline user file")
ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT , "Frontline Users"))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH ,"//button[contains(.,'Import CSV')]"))).click()
driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='contained-button-file']").send_keys("C:/Users/bitcot/Downloads/Frontline.csv")
time.sleep(5)
driver.find_element_by_xpath("//button[@id='delete']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Search By Id']").send_keys("FU123")
driver.find_element_by_xpath("//button[@id='submit']").click()
time.sleep(5)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('Frontline.png')
time.sleep(5)
print("Frontline user imported successfully with screenshot")
driver.close()