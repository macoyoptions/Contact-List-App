import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from AllLocators.All_Locators import LoginLocators, AddNewContactLocator, LogoutLocator


class ActionPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    # test for positive test
    def enter_gmail(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_GMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def clear_gmail(self):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_GMAIL))
        enter_email.clear()
        time.sleep(5)

    def clear_password(self):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_PASSWORD))
        enter_password.clear()
        time.sleep(5)

    def click_login(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.CLICK_LOGIN))
        click_submit.click()
        time.sleep(5)

    def get_error_message_element(self):
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ERROR_MESSAGE))
        return error_message_element

    # Fill in all the information required for the contact


class AddNewContactPage:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage1:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage2:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage3:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage4:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage5:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage6:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)

    def logout(self):
        click_logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocator.CLICK_LOGOUT))
        click_logout.click()
        time.sleep(5)


class AddNewContactPage7:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage8:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class AddNewContactPage9:
    def __init__(self, driver):
        self.driver = driver

    def add_new_contact(self):
        click_add_new_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContactLocator.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        click_logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocator.CLICK_LOGOUT))
        click_logout.click()
        time.sleep(5)

