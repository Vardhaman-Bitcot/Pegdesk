import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
found = False
while not found:
        try:
            Account_wait = ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Quotes")))
            found = True
            print("Sign In successfully")
        except (NoSuchElementException, TimeoutException) as e:
            time.sleep(2)
            print("Sign In error")
            driver.quit()
            exit()
time.sleep(3)
print("Check whether frontline user is able to scan and History")
ex_wait.until(EC.presence_of_element_located((By.XPATH , "//body[@class='body']/div[@id='root']/div[@class='app sidebar-mini rtl dashboard_page_body']/aside[@class='app-sidebar']/ul[@class='app-menu']/li[4]/a[1]"))).click()
driver.find_element_by_xpath('/html/body/div/div/aside/ul/li[4]/a/span[3]').click()
ex_wait.until(EC.element_to_be_clickable((By.XPATH , "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH , "//a[contains(@class,'btn btn-area')]"))).click()
driver.find_element_by_xpath("//button[contains(.,'Show QR')]").click()
time.sleep(15)
print("Scanned successfully via phone")
driver.find_element_by_xpath("//i[@class='fa fa-times']").click()
driver.find_element_by_xpath("//button[contains(@class,'btn btn-secondary float-right cst_btn mb-1')]").click()
driver.find_element_by_xpath("//a[@class='text_danger']").click()
found = False
while not found:
        try:
            ex_wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Superadmin | Bitcot')]")))
            found = True
            print("Passed")
        except (NoSuchElementException, TimeoutException) as e:
            time.sleep(2)
            print("Failed")
            exit()
time.sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB,Keys.TAB,"DD",Keys.TAB)
# actions.perform()
driver.quit()