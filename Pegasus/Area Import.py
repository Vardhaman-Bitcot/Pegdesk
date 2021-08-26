import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options= webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://qa.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
print("Login success")
time.sleep(5)
print("2.Check Whether able to import CSV area file")
driver.find_element_by_link_text("Jobs").click()
time.sleep(3)
ex_wait.until(EC.element_to_be_clickable((By.XPATH , "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH , "//a[contains(@class,'btn btn-area')]"))).click()
driver.find_element_by_xpath("//button[contains(@class,'btn btn-area btn_danger float-right mt-2 mr-3')]").click()
driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='contained-button-file']").send_keys("C:/Users/bitcot/Downloads/Area.csv")
time.sleep(5)
driver.find_element_by_xpath("//button[@id='delete']").click()
time.sleep(5)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('Area.png')
time.sleep(5)
print("Successfully Imported CSV file with screenshot")
driver.close()
