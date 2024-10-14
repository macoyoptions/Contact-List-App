import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from AllLocators.All_Locators import AllLocators


class ActionPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    # test for positive test
    def gmail(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_GMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def login(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_LOGIN))
        click_submit.click()
        time.sleep(5)

        # Fill in all the information required for a 1st contact
    def addnewcontact(self):
        click_addnewcontact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT))
        click_addnewcontact.click()
        time.sleep(5)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME))
        enter_firstname.send_keys(firstname)
        time.sleep(5)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME))
        enter_lastname.send_keys(lastname)
        time.sleep(5)

    def dob(self, dob):
        enter_dob = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB))
        enter_dob.send_keys(dob)
        time.sleep(5)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(5)

    def number(self, number):
        enter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER))
        enter_number.send_keys(number)
        time.sleep(5)

    def street(self, street):
        enter_street = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET))
        enter_street.send_keys(street)
        time.sleep(5)

    def strt(self, strt):
        enter_strt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT))
        enter_strt.send_keys(strt)
        time.sleep(5)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def postal(self, postal):
        enter_postal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL))
        enter_postal.send_keys(postal)
        time.sleep(5)

    def country(self, country):
        enter_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY))
        enter_country.send_keys(country)
        time.sleep(5)

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(5)

    # Fill in all the information required for a 2nd contact
    def addnewcontact1(self):
        click_addnewcontact1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_1))
        click_addnewcontact1.click()
        time.sleep(5)

    def firstname1(self, firstname1):
        enter_firstname1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_1))
        enter_firstname1.send_keys(firstname1)
        time.sleep(5)

    def lastname1(self, lastname1):
        enter_lastname1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_1))
        enter_lastname1.send_keys(lastname1)
        time.sleep(5)

    def dob1(self, dob1):
        enter_dob1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_1))
        enter_dob1.send_keys(dob1)
        time.sleep(5)

    def email1(self, email1):
        enter_email1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_1))
        enter_email1.send_keys(email1)
        time.sleep(5)

    def number1(self, number1):
        enter_number1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_1))
        enter_number1.send_keys(number1)
        time.sleep(5)

    def street1(self, street1):
        enter_street1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_1))
        enter_street1.send_keys(street1)
        time.sleep(5)

    def strt1(self, strt1):
        enter_strt1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_1))
        enter_strt1.send_keys(strt1)
        time.sleep(5)

    def city1(self, city1):
        enter_city1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_1))
        enter_city1.send_keys(city1)
        time.sleep(5)

    def state1(self, state1):
        enter_state1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_1))
        enter_state1.send_keys(state1)
        time.sleep(5)

    def postal1(self, postal1):
        enter_postal1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_1))
        enter_postal1.send_keys(postal1)
        time.sleep(5)

    def country1(self, country1):
        enter_country1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_1))
        enter_country1.send_keys(country1)
        time.sleep(5)

    def submit1(self):
        click_submit1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_1))
        click_submit1.click()
        time.sleep(5)

    # Fill in all the information required for a 3rd contact

    def addnewcontact2(self):
        click_addnewcontact2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_2))
        click_addnewcontact2.click()
        time.sleep(5)

    def firstname2(self, firstname2):
        enter_firstname2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_2))
        enter_firstname2.send_keys(firstname2)
        time.sleep(5)

    def lastname2(self, lastname2):
        enter_lastname2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_2))
        enter_lastname2.send_keys(lastname2)
        time.sleep(5)

    def dob2(self, dob2):
        enter_dob2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_2))
        enter_dob2.send_keys(dob2)
        time.sleep(5)

    def email2(self, email2):
        enter_email2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_2))
        enter_email2.send_keys(email2)
        time.sleep(5)

    def number2(self, number2):
        enter_number2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_2))
        enter_number2.send_keys(number2)
        time.sleep(5)

    def street2(self, street2):
        enter_street2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_2))
        enter_street2.send_keys(street2)
        time.sleep(5)

    def strt2(self, strt2):
        enter_strt2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_2))
        enter_strt2.send_keys(strt2)
        time.sleep(5)

    def city2(self, city2):
        enter_city2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_2))
        enter_city2.send_keys(city2)
        time.sleep(5)

    def state2(self, state2):
        enter_state2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_2))
        enter_state2.send_keys(state2)
        time.sleep(5)

    def postal2(self, postal2):
        enter_postal2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_2))
        enter_postal2.send_keys(postal2)
        time.sleep(5)

    def country2(self, country2):
        enter_country2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_2))
        enter_country2.send_keys(country2)
        time.sleep(5)

    def submit2(self):
        click_submit2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_2))
        click_submit2.click()
        time.sleep(5)

    # Fill in all the information required for a 4th contact
    def addnewcontact3(self):
        click_addnewcontact3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_3))
        click_addnewcontact3.click()
        time.sleep(5)

    def firstname3(self, firstname3):
        enter_firstname3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_3))
        enter_firstname3.send_keys(firstname3)
        time.sleep(5)

    def lastname3(self, lastname3):
        enter_lastname3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_3))
        enter_lastname3.send_keys(lastname3)
        time.sleep(5)

    def dob3(self, dob3):
        enter_dob3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_3))
        enter_dob3.send_keys(dob3)
        time.sleep(5)

    def email3(self, email3):
        enter_email3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_3))
        enter_email3.send_keys(email3)
        time.sleep(5)

    def number3(self, number3):
        enter_number3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_3))
        enter_number3.send_keys(number3)
        time.sleep(5)

    def street3(self, street3):
        enter_street3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_3))
        enter_street3.send_keys(street3)
        time.sleep(5)

    def strt3(self, strt3):
        enter_strt3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_3))
        enter_strt3.send_keys(strt3)
        time.sleep(5)

    def city3(self, city3):
        enter_city3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_3))
        enter_city3.send_keys(city3)
        time.sleep(5)

    def state3(self, state3):
        enter_state3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_3))
        enter_state3.send_keys(state3)
        time.sleep(5)

    def postal3(self, postal3):
        enter_postal3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_3))
        enter_postal3.send_keys(postal3)
        time.sleep(5)

    def country3(self, country3):
        enter_country3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_3))
        enter_country3.send_keys(country3)
        time.sleep(5)

    def submit3(self):
        click_submit3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_3))
        click_submit3.click()
        time.sleep(5)

    # Fill in all the information required for a 5th contact
    def addnewcontact4(self):
        click_addnewcontact4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_4))
        click_addnewcontact4.click()
        time.sleep(5)

    def firstname4(self, firstname4):
        enter_firstname4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_4))
        enter_firstname4.send_keys(firstname4)
        time.sleep(5)

    def lastname4(self, lastname4):
        enter_lastname4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_4))
        enter_lastname4.send_keys(lastname4)
        time.sleep(5)

    def dob4(self, dob4):
        enter_dob4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_4))
        enter_dob4.send_keys(dob4)
        time.sleep(5)

    def email4(self, email4):
        enter_email4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_4))
        enter_email4.send_keys(email4)
        time.sleep(5)

    def number4(self, number4):
        enter_number4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_4))
        enter_number4.send_keys(number4)
        time.sleep(5)

    def street4(self, street4):
        enter_street4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_4))
        enter_street4.send_keys(street4)
        time.sleep(5)

    def strt4(self, strt4):
        enter_strt4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_4))
        enter_strt4.send_keys(strt4)
        time.sleep(5)

    def city4(self, city4):
        enter_city4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_4))
        enter_city4.send_keys(city4)
        time.sleep(5)

    def state4(self, state4):
        enter_state4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_4))
        enter_state4.send_keys(state4)
        time.sleep(5)

    def postal4(self, postal4):
        enter_postal4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_4))
        enter_postal4.send_keys(postal4)
        time.sleep(5)

    def country4(self, country4):
        enter_country4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_4))
        enter_country4.send_keys(country4)
        time.sleep(5)

    def submit4(self):
        click_submit4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_4))
        click_submit4.click()
        time.sleep(5)

    # Fill in all the information required for a 6th contact
    def addnewcontact5(self):
        click_addnewcontact5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_5))
        click_addnewcontact5.click()
        time.sleep(5)

    def firstname5(self, firstname5):
        enter_firstname5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_5))
        enter_firstname5.send_keys(firstname5)
        time.sleep(5)

    def lastname5(self, lastname5):
        enter_lastname5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_5))
        enter_lastname5.send_keys(lastname5)
        time.sleep(5)

    def dob5(self, dob5):
        enter_dob5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_5))
        enter_dob5.send_keys(dob5)
        time.sleep(5)

    def email5(self, email5):
        enter_email5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_5))
        enter_email5.send_keys(email5)
        time.sleep(5)

    def number5(self, number5):
        enter_number5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_5))
        enter_number5.send_keys(number5)
        time.sleep(5)

    def street5(self, street5):
        enter_street5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_5))
        enter_street5.send_keys(street5)
        time.sleep(5)

    def strt5(self, strt5):
        enter_strt5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_5))
        enter_strt5.send_keys(strt5)
        time.sleep(5)

    def city5(self, city5):
        enter_city5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_5))
        enter_city5.send_keys(city5)
        time.sleep(5)

    def state5(self, state5):
        enter_state5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_5))
        enter_state5.send_keys(state5)
        time.sleep(5)

    def postal5(self, postal5):
        enter_postal5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_5))
        enter_postal5.send_keys(postal5)
        time.sleep(5)

    def country5(self, country5):
        enter_country5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_5))
        enter_country5.send_keys(country5)
        time.sleep(5)

    def submit5(self):
        click_submit5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_5))
        click_submit5.click()
        time.sleep(5)

    # Fill in all the information required for a 7th contact
    def addnewcontact6(self):
        click_addnewcontact6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_6))
        click_addnewcontact6.click()
        time.sleep(5)

    def firstname6(self, firstname6):
        enter_firstname6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_6))
        enter_firstname6.send_keys(firstname6)
        time.sleep(5)

    def lastname6(self, lastname6):
        enter_lastname6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_6))
        enter_lastname6.send_keys(lastname6)
        time.sleep(5)

    def dob6(self, dob6):
        enter_dob6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_6))
        enter_dob6.send_keys(dob6)
        time.sleep(5)

    def email6(self, email6):
        enter_email6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_6))
        enter_email6.send_keys(email6)
        time.sleep(5)

    def number6(self, number6):
        enter_number6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_6))
        enter_number6.send_keys(number6)
        time.sleep(5)

    def street6(self, street6):
        enter_street6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_6))
        enter_street6.send_keys(street6)
        time.sleep(5)

    def strt6(self, strt6):
        enter_strt6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_6))
        enter_strt6.send_keys(strt6)
        time.sleep(5)

    def city6(self, city6):
        enter_city6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_6))
        enter_city6.send_keys(city6)
        time.sleep(5)

    def state6(self, state6):
        enter_state6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_6))
        enter_state6.send_keys(state6)
        time.sleep(5)

    def postal6(self, postal6):
        enter_postal6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_6))
        enter_postal6.send_keys(postal6)
        time.sleep(5)

    def country6(self, country6):
        enter_country6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_6))
        enter_country6.send_keys(country6)
        time.sleep(5)

    def submit6(self):
        click_submit6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_6))
        click_submit6.click()
        time.sleep(5)

    # Fill in all the information required for an 8th contact
    def addnewcontact7(self):
        click_addnewcontact7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_7))
        click_addnewcontact7.click()
        time.sleep(5)

    def firstname7(self, firstname7):
        enter_firstname7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_7))
        enter_firstname7.send_keys(firstname7)
        time.sleep(5)

    def lastname7(self, lastname7):
        enter_lastname7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_7))
        enter_lastname7.send_keys(lastname7)
        time.sleep(5)

    def dob7(self, dob7):
        enter_dob7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_7))
        enter_dob7.send_keys(dob7)
        time.sleep(5)

    def email7(self, email7):
        enter_email7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_7))
        enter_email7.send_keys(email7)
        time.sleep(5)

    def number7(self, number7):
        enter_number7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_7))
        enter_number7.send_keys(number7)
        time.sleep(5)

    def street7(self, street7):
        enter_street7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_7))
        enter_street7.send_keys(street7)
        time.sleep(5)

    def strt7(self, strt7):
        enter_strt7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_7))
        enter_strt7.send_keys(strt7)
        time.sleep(5)

    def city7(self, city7):
        enter_city7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_7))
        enter_city7.send_keys(city7)
        time.sleep(5)

    def state7(self, state7):
        enter_state7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_7))
        enter_state7.send_keys(state7)
        time.sleep(5)

    def postal7(self, postal7):
        enter_postal7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_7))
        enter_postal7.send_keys(postal7)
        time.sleep(5)

    def country7(self, country7):
        enter_country7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_7))
        enter_country7.send_keys(country7)
        time.sleep(5)

    def submit7(self):
        click_submit7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_7))
        click_submit7.click()
        time.sleep(5)

    # Fill in all the information required for a 9th contact
    def addnewcontact8(self):
        click_addnewcontact8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_8))
        click_addnewcontact8.click()
        time.sleep(5)

    def firstname8(self, firstname8):
        enter_firstname8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_8))
        enter_firstname8.send_keys(firstname8)
        time.sleep(5)

    def lastname8(self, lastname8):
        enter_lastname8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_8))
        enter_lastname8.send_keys(lastname8)
        time.sleep(5)

    def dob8(self, dob8):
        enter_dob8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_8))
        enter_dob8.send_keys(dob8)
        time.sleep(5)

    def email8(self, email8):
        enter_email8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_8))
        enter_email8.send_keys(email8)
        time.sleep(5)

    def number8(self, number8):
        enter_number8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_8))
        enter_number8.send_keys(number8)
        time.sleep(5)

    def street8(self, street8):
        enter_street8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_8))
        enter_street8.send_keys(street8)
        time.sleep(5)

    def strt8(self, strt8):
        enter_strt8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_8))
        enter_strt8.send_keys(strt8)
        time.sleep(5)

    def city8(self, city8):
        enter_city8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_8))
        enter_city8.send_keys(city8)
        time.sleep(5)

    def state8(self, state8):
        enter_state8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_8))
        enter_state8.send_keys(state8)
        time.sleep(5)

    def postal8(self, postal8):
        enter_postal8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_8))
        enter_postal8.send_keys(postal8)
        time.sleep(5)

    def country8(self, country8):
        enter_country8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_8))
        enter_country8.send_keys(country8)
        time.sleep(5)

    def submit8(self):
        click_submit8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_8))
        click_submit8.click()
        time.sleep(5)

    # Fill in all the information required for a 10th contact
    def addnewcontact9(self):
        click_addnewcontact9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_ADD_NEW_CONTACT_9))
        click_addnewcontact9.click()
        time.sleep(5)

    def firstname9(self, firstname9):
        enter_firstname9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_FIRST_NAME_9))
        enter_firstname9.send_keys(firstname9)
        time.sleep(5)

    def lastname9(self, lastname9):
        enter_lastname9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_LAST_NAME_9))
        enter_lastname9.send_keys(lastname9)
        time.sleep(5)

    def dob9(self, dob9):
        enter_dob9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_DOB_9))
        enter_dob9.send_keys(dob9)
        time.sleep(5)

    def email9(self, email9):
        enter_email9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_EMAIL_9))
        enter_email9.send_keys(email9)
        time.sleep(5)

    def number9(self, number9):
        enter_number9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_NUMBER_9))
        enter_number9.send_keys(number9)
        time.sleep(5)

    def street9(self, street9):
        enter_street9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STREET_9))
        enter_street9.send_keys(street9)
        time.sleep(5)

    def strt9(self, strt9):
        enter_strt9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STRT_9))
        enter_strt9.send_keys(strt9)
        time.sleep(5)

    def city9(self, city9):
        enter_city9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_CITY_9))
        enter_city9.send_keys(city9)
        time.sleep(5)

    def state9(self, state9):
        enter_state9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_STATE_9))
        enter_state9.send_keys(state9)
        time.sleep(5)

    def postal9(self, postal9):
        enter_postal9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_POSTAL_9))
        enter_postal9.send_keys(postal9)
        time.sleep(5)

    def country9(self, country9):
        enter_country9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.ENTER_COUNTRY_9))
        enter_country9.send_keys(country9)
        time.sleep(5)

    def submit9(self):
        click_submit9 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_SUBMIT_9))
        click_submit9.click()
        time.sleep(5)

    def logout(self):
        click_logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.CLICK_LOGOUT))
        click_logout.click()
        time.sleep(5)

        # for negative login
    def negativegmail(self, gmail):
        enter_gmail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.NEGATIVE_ENTER_GMAIL))
        enter_gmail.send_keys(gmail)
        time.sleep(5)

    def negativepassword(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.NEGATIVE_ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def negativelogin(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AllLocators.NEGATIVE_CLICK_LOGIN))
        click_submit.click()
        time.sleep(5)

