import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from SignupLocator.Signup_Locator import SignupLocator


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    def signup_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    def signup(self):
        click_signup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.CLICK_SIGNUP_BUTTON))
        click_signup.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignupLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)
