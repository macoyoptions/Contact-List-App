import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LogoutLocator.Logout_locator import LogoutLocator


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        click_logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocator.CLICK_LOGOUT))
        click_logout.click()
        time.sleep(5)

