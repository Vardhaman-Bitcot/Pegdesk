import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://staging-node.pegdesk.com/")
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 30)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'Inspections')]").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@class='btn btn-secondary cst_btn']").click()
time.sleep(20)
driver.find_element_by_xpath("//div[@id='addAccountModal']/div/div/form/div/div/div/div/div/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='react-select-8-input']").send_keys("Bitcot technology", Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(2)
driver.find_element_by_css_selector(".css-t2qm4o-control > .css-1hwfws3").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='react-select-9-input']").send_keys("Abstract", Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
time.sleep(5)

#Create Quote
driver.find_element_by_xpath("//div[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][0][comment]']//button[@class='btn btn_danger'][contains(text(),'Create Quote')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='total_sale']").send_keys("500")
driver.find_element_by_xpath("//textarea[@id='comment']").send_keys("Firefox clears your search and browsing history when you quit the app or close all Private Browsing tabs and windows.")
driver.find_element_by_xpath("//button[contains(text(),'Submit Now')]").click()
time.sleep(5)
#driver.find_element_by_xpath("//button[contains(text(),'Submit Later')]").click()                     Later
#driver.find_element_by_xpath("//button[@class='btn cst_btn btn-outline-secondary']").click()          Cancel

#Create Ticket
driver.find_element_by_xpath("//button[@class='btn danger_light_btn']").click()
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
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
Select (driver.find_element_by_xpath("//select[@name='ticket[priority]']")).select_by_value("5")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='file_attachment']//input").send_keys("C:/Users/bitcot/Pictures/bitcot.jpg")
time.sleep(3)
driver.find_element_by_xpath("//button[@class='btn cst_btn btn_danger']").click()
time.sleep(10)
driver.find_element_by_xpath("//input[@name='subject']").send_keys("My First")
time.sleep(3)
driver.find_element_by_xpath("//button[@id='submit']").click()
time.sleep(3)

#inspection form
add = Select(driver.find_element_by_xpath("//select[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][0][rating_option_id]']"))
add.select_by_value("79")
time.sleep(2)
driver.find_element_by_id("exampleFormControlTextarea1").send_keys("Hi this automation from bitcot testing the application")
#driver.find_element_by_xpath("//div[@id='file-upload-wrapper00']").send_keys("")   upload

sub = Select(driver.find_element_by_xpath("//select[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][1][rating_option_id]']"))
sub.select_by_value("78")
time.sleep(2)
driver.find_element_by_xpath("//div[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][1][comment]']//textarea[@id='exampleFormControlTextarea1']").send_keys("Now you can browse privately, and other people who use this device won't see your activity. However, downloads and bookmarks will be saved.")
#driver.find_element_by_xpath("//div[@id='file-upload-wrapper01']").send_keys("")    upload

mul = Select(driver.find_element_by_xpath("//select[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][2][rating_option_id]']"))
mul.select_by_visible_text("Yes")
time.sleep(2)
driver.find_element_by_xpath("//div[@name='inspection[inspection_form][sections_attributes][0][line_items_attributes][2][comment]']//textarea[@id='exampleFormControlTextarea1']").send_keys("Firefox clears your search and browsing history when you quit the app or close all Private Browsing tabs and windows. While this doesn’t make you anonymous to web sites or your internet service provider, it makes it easier to keep what you do online private from anyone else who uses this computer.")
#driver.find_element_by_xpath("//div[@id='file-upload-wrapper02']").send_keys()      upload

driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()