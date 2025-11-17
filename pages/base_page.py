import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_random_element(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return random.choice(elements).click()

    def type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def resolve_js(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

