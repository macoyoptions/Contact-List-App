from selenium.webdriver.common.by import By


class LoginLocators:
    ENTER_GMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    CLICK_LOGIN = (By.XPATH, '//*[@id="submit"]')
    ERROR_MESSAGE = (By.ID, "error")


class AddNewContactLocator:
    CLICK_ADD_NEW_CONTACT = (By.XPATH, "/html/body/div/p[2]/button")
    ENTER_FIRST_NAME = (By.ID, "firstName")
    ENTER_LAST_NAME = (By.XPATH, "/html/body/div/form/p[1]/input[2]")
    ENTER_DOB = (By.ID, "birthdate")
    ENTER_EMAIL = (By.ID, "email")
    ENTER_NUMBER = (By.ID, "phone")
    ENTER_STREET = (By.ID, "street1")
    ENTER_STRT = (By.ID, "street2")
    ENTER_CITY = (By.ID, "city")
    ENTER_STATE = (By.ID, "stateProvince")
    ENTER_POSTAL = (By.ID, "postalCode")
    ENTER_COUNTRY = (By.ID, "country")
    CLICK_SUBMIT = (By.ID, "submit")


class LogoutLocator:
    CLICK_LOGOUT = (By.XPATH, "/html/body/div/header/button")
