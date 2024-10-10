from selenium.webdriver.common.by import By


class SignupLocator:
    CLICK_SIGNUP_BUTTON = (By.XPATH, "/html/body/div[3]/button")
    ENTER_FIRST_NAME = (By.XPATH, "/html/body/div/form/p[1]/input")
    ENTER_LAST_NAME = (By.XPATH, "/html/body/div/form/p[2]/input")
    ENTER_EMAIL = (By.XPATH, "/html/body/div/form/p[3]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div/form/p[4]/input")
    CLICK_SUBMIT = (By.XPATH, "/html/body/div/p[2]/button[1]")
