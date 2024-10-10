import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LoginLocator.Login_Locator import LoginLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    # test for positive test

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)

# test for negative login
# FOR NEGATIVE TEST, FILL IN EMAIL THAT IS ALREADY IN USE
    def old_email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_OLD_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def passwordd(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_PASSWORDD))
        enter_password.send_keys(password)
        time.sleep(5)

    def submitt(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.CLICK_SUBMITT))
        click_submit.click()
        time.sleep(5)
