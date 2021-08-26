import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C://Users/bitcot/PycharmProjects/Pegasus_Unittest/Package/chromedriver.exe")
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.driver.get("https://qa.pegdesk.com/")
        print("Project title is: ", cls.driver.title)
        cls.ex_wait = WebDriverWait(cls.driver, 30)
        print("1.Check whether superadmin is able to sign in Successfully with given login ")
        cls.driver.find_element_by_name("user[email]").send_keys("dev@bitcot.com")
        cls.driver.find_element_by_name("user[password]").send_keys("bitcotadmin")
        cls.driver.find_element_by_xpath("(//button)[contains(text(),'Sign In')]").click()
        found = False
        while not found:
            try:
                cls.ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Dashboard")))
                found = True
                print("Login success")
            except (NoSuchElementException, TimeoutException) as e:
                time.sleep(2)
                print("Login error")
                exit()
        time.sleep(2)

    def send_keys_delayed(self, elementName, str):
        for char in str:
            self.driver.find_element_by_name(elementName).send_keys(char)
            time.sleep(random.uniform(0.03, 0.2))

    def test_account_create(self):
        print("2.Check whether superadmin is able to create account successfully")
        self.ex_wait.until(EC.presence_of_element_located((By.XPATH,"//body[@class='body']/div[@id='root']/div[@class='app sidebar-mini rtl dashboard_page_body']/aside[@class='app-sidebar']/ul[@class='app-menu']/li[4]/a[1]"))).click()
        self.driver.find_element_by_xpath('/html/body/div/div/aside/ul/li[4]/a/span[3]').click()
        self.driver.find_element_by_xpath("//a[@class='btn btn-secondary cst_btn']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@name='account[name]']").send_keys("Automation")
        self.driver.find_element_by_xpath("//input[@name='account[account_number]']").send_keys("2000")
        self.driver.find_element_by_xpath("//input[@id='googleAddress']").send_keys("92127")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='autocomplete-dropdown-container']//div[1]").click()
        time.sleep(2)
        Selector = Select(self.driver.find_element_by_name("account[region_id]"))
        Selector.select_by_index(10)
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button)[contains(text(),'Submit')]").clik()
        time.sleep(2)
        found = False
        while not found:
            try:
                self.ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Go')]")))
                found = True
                print("Account created successfully")
            except (NoSuchElementException, TimeoutException) as e:
                time.sleep(2)
                print("Unable to create the account:", 'Account Number has already been taken')
                exit()
        time.sleep(3)

    def test_associate_account(self):
        print("3. Check whether superadmin able to associate with this account")
        self.ex_wait.until(EC.presence_of_element_located((By.XPATH,
                                                           "//body[@class='body']/div[@id='root']/div[@class='app sidebar-mini rtl dashboard_page_body']/aside[@class='app-sidebar']/ul[@class='app-menu']/li[4]/a[1]"))).click()
        self.driver.find_element_by_xpath('/html/body/div/div/aside/ul/li[4]/a/span[3]').click()
        self.ex_wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Associate User')]").click()
        time.sleep(5)
        actions = ActionChains(self.driver)
        answer = actions.send_keys(Keys.TAB, Keys.TAB, "testqa@bitcot.com", Keys.TAB)
        actions.perform()
        time.sleep(3)
        if answer == 'testqa+test@bitcot.com':
            print("Email Id is matching")
        else:
            print("email is not match")
            exit()
        self.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        time.sleep(3)

    def test_fontline_user(self):
        print("4. Check whether superadmin is able to create fronline user")
        self.ex_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Frontline Users"))).click()
        self.ex_wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='float-right btn btn-secondary cst_btn mr-1 mb-1 min-width-btn']"))).click()
        self.driver.find_element_by_xpath("//input[@id='first_name']").send_keys("Automation")
        self.driver.find_element_by_xpath("//input[@id='last_name']").send_keys("User")
        self.driver.find_element_by_xpath("//div[4]//input[1]").send_keys("Fresh")
        found = False
        while not found:
            try:
                self.ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Import CSV')]")))
                found = True
                print("Frontline user is created successfully")
            except (NoSuchElementException, TimeoutException) as e:
                time.sleep(2)
                print("Unable to create frontline user:", 'Employee ID has already been taken')
                exit()
        self.send_keys_delayed("frontline[dob_password]", "9999")
        self.driver.find_element_by_name("frontline[dob_password]").send_keys(Keys.TAB, "Automation", Keys.ARROW_UP,
                                                                              Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@class='btn cst_btn btn_danger mr-2']").click()

    def test_create_area(self):
        print("5. Check whether area is created in account")
        self.driver.find_element_by_xpath("//span[contains(.,'Accounts')]").click()
        self.ex_wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//i)[@class='fas fa-eye cst_icon mr-2'][1] "))).click()
        self.ex_wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'btn btn-area')]"))).click()
        self.ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Area')]"))).click()
        time.sleep(3)
        self.driver.find_element_by_id("areaName").send_keys("Legend")
        floor = Select(self.driver.find_element_by_name("area[floor_id]"))
        floor.select_by_index(2)
        area = Select(self.driver.find_element_by_name("area[area_type_id]"))
        area.select_by_index(2)
        self.driver.execute_script("window.scrollTo(0,1000);")
        self.driver.find_element_by_xpath("//label[contains(text(),'Sun')]").click()
        time.sleep(2)
        select_time = self.driver.find_element_by_name("area[timeslots_attributes][0][start_time]").click()
        default_hours = 12
        default_mins = 0
        hours = 8
        minutes = 45
        # am-0 pm-1
        am_pm = 0
        if (hours > 6):
            xpath_generator = 2
            flag = 2  # Flag is used to control am
        else:
            xpath_generator = 1
            flag = 1  # Flag is used to control pm
        if (hours < 6):
            differnce_hours = hours
        else:
            differnce_hours = default_hours - hours  # 12-8 =4
        print(default_hours, hours)
        print(differnce_hours)
        Arrow_button_wait = self.ex_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rdtBtn")))
        while (differnce_hours != -1):
            print("Inside hours loop")
            Arrow_button = self.driver.find_element_by_xpath(
                "(//span)[@class='rdtBtn'][" + str(xpath_generator) + "]").click()
            differnce_hours = differnce_hours - 1
        if (minutes < 30):
            xpath_generator = 3
        else:
            xpath_generator = 4
        differnce_mins = minutes - default_mins
        while (differnce_mins != 0):
            print("Inside minutes loop")
            Arrow_button = self.driver.find_element_by_xpath(
                "(//span)[@class='rdtBtn'][" + str(xpath_generator) + "]").click()
            differnce_mins = differnce_mins - 5
        if (am_pm == 1 and flag == 1 or am_pm == 0 and flag == 2):
            # flag - 2 (That means moving the time backwards)
            # am_pm =1 (pm Moving ahead will change
            print("Inside am/pm condition")
            xpath_generator = 5
            Arrow_button = self.driver.find_element_by_xpath(
                "(//span)[@class='rdtBtn'][" + str(xpath_generator) + "]").click()
        # driver.execute_script("arguments[0].value = '03:00 AM';",a)
        # driver.find_element_by_name("body").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        found = False
        while not found:
            try:
                self.ex_wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Reset')]")))
                found = True
                print("Area is created successfully")
            except (NoSuchElementException, TimeoutException) as e:
                time.sleep(2)
                print("Unable to create a area on this account: Area name has already been taken")
                exit()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(.,'Reset')]").click()

    def test_Scan_History(self):
        print("6. check whether the QR code generated and client URL History presented after scanned the QR code")
        self.driver.find_element_by_css_selector(".rt-td > .btn:nth-child(1)").click()
        time.sleep(15)
        print("Scanned successfully via phone")
        self.driver.find_element_by_xpath("//i[@class='fa fa-times']").click()
        self.driver.find_element_by_xpath("//button[contains(@class,'btn btn-secondary float-right cst_btn mb-1')]").click()
        self.driver.find_element_by_xpath("//a[@class='text_danger']").click()
        print("History is visible for the scanned area")
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
