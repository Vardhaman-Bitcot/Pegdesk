import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://qa.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1.Check whether superadmin is able to sign in successfully")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
time.sleep(5)
print("Sign In Successfully")
driver.find_element_by_link_text("Quotes").click()
print("2.Check whether superadmin is able to create new quote and manual quote")
driver.find_element_by_xpath("//a[contains(text(),'New Quote')]").click()
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class,'css-1hwfws3')]").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='react-select-3-input']").send_keys("Bitcot Technology", Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("//input[@id='total_sale']").send_keys("1000")
driver.find_element_by_xpath("//textarea[@id='comment']").send_keys("New Quote created using selenium automate for internal testing")
driver.find_element_by_xpath("//button[contains(text(),'Submit Now')]").click()
time.sleep(5)
#driver.find_element_by_xpath("//button[contains(text(),'Submit Later')]").click()
driver.find_element_by_xpath("//input[@name='name']").send_keys("Bitcot Technology")
driver.find_element_by_xpath("//button[@id='submit']").click()
time.sleep(5)
driver.save_screenshot("new.png")
print("Successfully Created New Quote with screenshot by filter")
driver.quit()
