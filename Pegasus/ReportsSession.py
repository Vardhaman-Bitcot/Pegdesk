import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.headless = True
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.get("https://staging-node.pegdesk.com/")
        print("Project title is: ", cls.driver.title)
        cls.ex_wait = WebDriverWait(cls.driver, 15)
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
    def filter_Quotes(self):
        print("2. Check the reports page with all tabs")
        print("2.1 Quotes Filter: ")
        time.sleep(2)
        self.driver.find_element_by_link_text("Reports").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//li/div/div/div/div").click()
        self.driver.find_element_by_xpath("//div[@id='react-select-2-option-0-0']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//label/div/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[@id='basic-addon2']/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--001']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[2]/label/div[2]/span/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--015 react-datepicker__day--keyboard-selected react-datepicker__day--today']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        print("Quotes Filter is shown with full page screenshot")
        #Full page screenshot
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
        self.driver.set_window_size(S('Width'), S('Height'))
        self.driver.find_element_by_tag_name('body').screenshot('rqp.png')
        time.sleep(10)

    def filter_PegAssure(self):
        print("2.2 PagAssure Filter:")
        self.driver.find_element_by_xpath("//button[contains(.,'PegAssure')]").click()
        time.sleep(10)
        self.driver.find_element_by_class_name("css-1hwfws3").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[2]/div/div/div[2]/div").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[2]/div/div/div/div").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='react-select-4-option-0-0']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[@class='feed-item mt-2']//div[1]//div[2]//span[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--001']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("(//span[@id='basic-addon2']/img)[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--015 react-datepicker__day--keyboard-selected react-datepicker__day--today']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        print("PegAssure Filter is shown with full page screenshot")
        # Full page screenshot
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll' + X)
        self.driver.set_window_size(S('Width'), S('Height'))
        self.driver.find_element_by_tag_name('body').screenshot('rpap.png')
        time.sleep(5)
    def filter_Inspection(self):
        print("2.3 Inspection Reports:")
        self.driver.find_element_by_xpath("//button[contains(.,'Inspection Reports')]").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector(".css-1hwfws3").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='react-select-3-option-0-0']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[@id='basic-addon2']/i").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--001']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//span[@id='basic-addon2'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--015 react-datepicker__day--keyboard-selected react-datepicker__day--today']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
        time.sleep(5)
        print("Inspection Reports Filter is shown with full page screenshot")
        # Full page screenshot
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll' + X)
        self.driver.set_window_size(S('Width'), S('Height'))
        self.driver.find_element_by_tag_name('body').screenshot('rpap.png')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

