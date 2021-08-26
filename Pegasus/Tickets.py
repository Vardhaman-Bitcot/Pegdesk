import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://staging-node.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 30)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
print("Login success")
time.sleep(5)
print("2.Check whether superadmin is able to create tickets")
driver.find_element_by_link_text("Tickets").click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(@class,'btn btn-secondary cst_btn')]").click()
time.sleep(5)
driver.find_element_by_class_name("css-1hwfws3").click()
time.sleep(2)
driver.find_element_by_id("react-select-2-option-12").click()
time.sleep(3)
ticket= Select (driver.find_element_by_css_selector("[name='ticket[category_id]']"))
ticket.select_by_value("19")
driver.find_element_by_css_selector("[name='ticket[subject]']").send_keys("My First")
driver.find_element_by_css_selector("#comment").send_keys("Automation testing on the pegasus application")
driver.find_element_by_xpath("//div[6]/div").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='react-select-3-option-0']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@placeholder='To Date']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--002']").click()
Select (driver.find_element_by_xpath("//select[@name='ticket[priority]']")).select_by_value("5")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='file_attachment']//input").send_keys("C:/Users/bitcot/Pictures/bitcot.jpg")
time.sleep(3)
driver.find_element_by_xpath("//button[@class='btn cst_btn btn_danger']").click()
time.sleep(10)
driver.find_element_by_xpath("//input[@name='subject']").send_keys("My First")
time.sleep(3)
driver.find_element_by_xpath("//button[@id='submit']").click()
time.sleep(5)
driver.save_screenshot('tic.png')
time.sleep(3)
print("Ticket created successfully with screenshot")
driver.quit()