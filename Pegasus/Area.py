import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get(config.URL)
print("Project title is: ", driver.title)
ex_wait = WebDriverWait(driver, 15)
print("1.Check whether superadmin is able to sign in Successfully with given login ")
driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
sign_in = driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
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
print("2.Check Whether able to create area")
driver.find_element_by_link_text("Jobs").click()
time.sleep(3)
ex_wait.until(EC.element_to_be_clickable((By.XPATH , "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH , "//a[contains(@class,'btn btn-area')]"))).click()
ex_wait.until(EC.presence_of_element_located((By.XPATH ,"//button[contains(text(),'Area')]"))).click()
time.sleep(3)
driver.find_element_by_id("areaName").send_keys("Legend")
floor = Select(driver.find_element_by_name("area[floor_id]"))
floor.select_by_index(2)
area = Select(driver.find_element_by_name("area[area_type_id]"))
area.select_by_index(2)
driver.execute_script("window.scrollTo(0,1000);")
driver.find_element_by_xpath("//label[contains(text(),'Sun')]").click()
driver.find_element_by_css_selector(".from-date-analytics").click()
driver.find_element_by_css_selector(".react-datepicker__day--keyboard-selected").click()
time.sleep(3)
time.sleep(2)
select_time = driver.find_element_by_name("area[timeslots_attributes][0][start_time]").click()
default_hours=12
default_mins = 0
hours = 8
minutes = 45
#am-0 pm-1
am_pm = 0
if(hours>6):
    xpath_generator=2
    flag=2 # Flag is used to control am
else:
    xpath_generator=1
    flag=1 # Flag is used to control pm
if(hours<6):
    differnce_hours = hours
else:
    differnce_hours = default_hours - hours  # 12-8 =4
print(default_hours,hours)
print(differnce_hours)
Arrow_button_wait = ex_wait.until(EC.element_to_be_clickable((By.CLASS_NAME , "rdtBtn")))
while(differnce_hours!=-1):
    print("Inside hours loop")
    Arrow_button = driver.find_element_by_xpath("(//span)[@class='rdtBtn']["+str(xpath_generator)+"]").click()
    differnce_hours=differnce_hours-1
if(minutes<30):
    xpath_generator=3
else:
    xpath_generator=4
differnce_mins = minutes-default_mins
while(differnce_mins!=0):
    print("Inside minutes loop")
    Arrow_button = driver.find_element_by_xpath("(//span)[@class='rdtBtn']["+str(xpath_generator)+"]").click()
    differnce_mins=differnce_mins-5
if(am_pm==1 and flag==1 or am_pm==0 and flag==2):
    print("Inside am/pm condition")
    xpath_generator = 5
    Arrow_button = driver.find_element_by_xpath("(//span)[@class='rdtBtn'][" + str(xpath_generator) + "]").click()
driver.find_element_by_xpath("//button[@type='submit']").click()
found = False
while not found:
        try:
            ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Reset')]")))
            found = True
            print("Area is created successfully")
        except (NoSuchElementException, TimeoutException) as e:
            time.sleep(2)
            print("Unable to create a area on this account: Area name has already been taken")
            driver.quit()
            exit()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(.,'Reset')]").click()
driver.close()
