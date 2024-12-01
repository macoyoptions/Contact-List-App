import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ActionPage.ActionPage_test import ActionPage, LogoutPage, AddNewContactPage9, AddNewContactPage8, \
    AddNewContactPage7, AddNewContactPage6, AddNewContactPage5, AddNewContactPage4, AddNewContactPage3, \
    AddNewContactPage2, AddNewContactPage1, AddNewContactPage
from config.config import Config, ConfigAddNewContact9, ConfigAddNewContact8, ConfigAddNewContact7, \
    ConfigAddNewContact6, ConfigAddNewContact5, ConfigAddNewContact4, ConfigAddNewContact3, ConfigAddNewContact2, \
    ConfigAddNewContact1, ConfigAddNewContact


@pytest.fixture(scope="session")
def driver_setup():
    firefox_options = Options()
    # Uncomment the line below to run in headless mode
    firefox_options.add_argument("--headless")  # Run Firefox in headless mode
    firefox_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = ActionPage(driver)
    login_page.login_url(Config.BASEURL)
    return login_page


def test_negative_login_page_contact_list(login):
    login.enter_gmail(Config.NEGATIVE_EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_login()
    login.clear_gmail()
    login.clear_password()

    # Verify the error message
    error_message_element = login.get_error_message_element()
    error_message = error_message_element.text
    assert "Incorrect username or password" in error_message, \
        "Error message does not match expected."

    print("Negative test passed: Incorrect username or password")


# positive login
def test_positive_login_page_contact_list(login):
    login.enter_gmail(Config.GMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_login()


def test_add_new_contact_contact_list(login):
    add_new_contact = AddNewContactPage(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact.FIRSTNAME)
    add_new_contact.lastname(ConfigAddNewContact.LASTNAME)
    add_new_contact.dob(ConfigAddNewContact.DOB)
    add_new_contact.email(ConfigAddNewContact.EMAIL)
    add_new_contact.number(ConfigAddNewContact.NUMBER)
    add_new_contact.street(ConfigAddNewContact.STREET)
    add_new_contact.city(ConfigAddNewContact.CITY)
    add_new_contact.state(ConfigAddNewContact.STATE)
    add_new_contact.postal(ConfigAddNewContact.POSTAL)
    add_new_contact.country(ConfigAddNewContact.COUNTRY)
    add_new_contact.submit()


def test_add_new_contact_contact_list1(login):
    add_new_contact = AddNewContactPage1(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact1.FIRSTNAME1)
    add_new_contact.lastname(ConfigAddNewContact1.LASTNAME1)
    add_new_contact.dob(ConfigAddNewContact1.DOB1)
    add_new_contact.email(ConfigAddNewContact1.EMAIL1)
    add_new_contact.number(ConfigAddNewContact1.NUMBER1)
    add_new_contact.street(ConfigAddNewContact1.STREET1)
    add_new_contact.city(ConfigAddNewContact1.CITY1)
    add_new_contact.state(ConfigAddNewContact1.STATE1)
    add_new_contact.postal(ConfigAddNewContact1.POSTAL1)
    add_new_contact.country(ConfigAddNewContact1.COUNTRY1)
    add_new_contact.submit()


def test_add_new_contact_contact_list2(login):
    add_new_contact = AddNewContactPage2(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact2.FIRSTNAME2)
    add_new_contact.lastname(ConfigAddNewContact2.LASTNAME2)
    add_new_contact.dob(ConfigAddNewContact2.DOB2)
    add_new_contact.email(ConfigAddNewContact2.EMAIL2)
    add_new_contact.number(ConfigAddNewContact2.NUMBER2)
    add_new_contact.street(ConfigAddNewContact2.STREET2)
    add_new_contact.city(ConfigAddNewContact2.CITY2)
    add_new_contact.state(ConfigAddNewContact2.STATE2)
    add_new_contact.postal(ConfigAddNewContact2.POSTAL2)
    add_new_contact.country(ConfigAddNewContact2.COUNTRY2)
    add_new_contact.submit()


def test_add_new_contact_contact_list3(login):
    add_new_contact = AddNewContactPage3(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact3.FIRSTNAME3)
    add_new_contact.lastname(ConfigAddNewContact3.LASTNAME3)
    add_new_contact.dob(ConfigAddNewContact3.DOB3)
    add_new_contact.email(ConfigAddNewContact3.EMAIL3)
    add_new_contact.number(ConfigAddNewContact3.NUMBER3)
    add_new_contact.street(ConfigAddNewContact3.STREET3)
    add_new_contact.city(ConfigAddNewContact3.CITY3)
    add_new_contact.state(ConfigAddNewContact3.STATE3)
    add_new_contact.postal(ConfigAddNewContact3.POSTAL3)
    add_new_contact.country(ConfigAddNewContact3.COUNTRY3)
    add_new_contact.submit()


def test_add_new_contact_contact_list4(login):
    add_new_contact = AddNewContactPage4(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact4.FIRSTNAME4)
    add_new_contact.lastname(ConfigAddNewContact4.LASTNAME4)
    add_new_contact.dob(ConfigAddNewContact4.DOB4)
    add_new_contact.email(ConfigAddNewContact4.EMAIL4)
    add_new_contact.number(ConfigAddNewContact4.NUMBER4)
    add_new_contact.street(ConfigAddNewContact4.STREET4)
    add_new_contact.city(ConfigAddNewContact4.CITY4)
    add_new_contact.state(ConfigAddNewContact4.STATE4)
    add_new_contact.postal(ConfigAddNewContact4.POSTAL4)
    add_new_contact.country(ConfigAddNewContact4.COUNTRY4)
    add_new_contact.submit()


def test_add_new_contact_contact_list5(login):
    add_new_contact = AddNewContactPage5(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact5.FIRSTNAME5)
    add_new_contact.lastname(ConfigAddNewContact5.LASTNAME5)
    add_new_contact.dob(ConfigAddNewContact5.DOB5)
    add_new_contact.email(ConfigAddNewContact5.EMAIL5)
    add_new_contact.number(ConfigAddNewContact5.NUMBER5)
    add_new_contact.street(ConfigAddNewContact5.STREET5)
    add_new_contact.city(ConfigAddNewContact5.CITY5)
    add_new_contact.state(ConfigAddNewContact5.STATE5)
    add_new_contact.postal(ConfigAddNewContact5.POSTAL5)
    add_new_contact.country(ConfigAddNewContact5.COUNTRY5)
    add_new_contact.submit()


def test_add_new_contact_contact_list6(login):
    add_new_contact = AddNewContactPage6(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact6.FIRSTNAME6)
    add_new_contact.lastname(ConfigAddNewContact6.LASTNAME6)
    add_new_contact.dob(ConfigAddNewContact6.DOB6)
    add_new_contact.email(ConfigAddNewContact6.EMAIL6)
    add_new_contact.number(ConfigAddNewContact6.NUMBER6)
    add_new_contact.street(ConfigAddNewContact6.STREET6)
    add_new_contact.city(ConfigAddNewContact6.CITY6)
    add_new_contact.state(ConfigAddNewContact6.STATE6)
    add_new_contact.postal(ConfigAddNewContact6.POSTAL6)
    add_new_contact.country(ConfigAddNewContact6.COUNTRY6)
    add_new_contact.submit()


def test_add_new_contact_contact_list7(login):
    add_new_contact = AddNewContactPage7(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact7.FIRSTNAME7)
    add_new_contact.lastname(ConfigAddNewContact7.LASTNAME7)
    add_new_contact.dob(ConfigAddNewContact7.DOB7)
    add_new_contact.email(ConfigAddNewContact7.EMAIL7)
    add_new_contact.number(ConfigAddNewContact7.NUMBER7)
    add_new_contact.street(ConfigAddNewContact7.STREET7)
    add_new_contact.city(ConfigAddNewContact7.CITY7)
    add_new_contact.state(ConfigAddNewContact7.STATE7)
    add_new_contact.postal(ConfigAddNewContact7.POSTAL7)
    add_new_contact.country(ConfigAddNewContact7.COUNTRY7)
    add_new_contact.submit()


def test_add_new_contact_contact_list8(login):
    add_new_contact = AddNewContactPage8(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact8.FIRSTNAME8)
    add_new_contact.lastname(ConfigAddNewContact8.LASTNAME8)
    add_new_contact.dob(ConfigAddNewContact8.DOB8)
    add_new_contact.email(ConfigAddNewContact8.EMAIL8)
    add_new_contact.number(ConfigAddNewContact8.NUMBER8)
    add_new_contact.street(ConfigAddNewContact8.STREET8)
    add_new_contact.city(ConfigAddNewContact8.CITY8)
    add_new_contact.state(ConfigAddNewContact8.STATE8)
    add_new_contact.postal(ConfigAddNewContact8.POSTAL8)
    add_new_contact.country(ConfigAddNewContact8.COUNTRY8)
    add_new_contact.submit()


def test_add_new_contact_contact_list9(login):
    add_new_contact = AddNewContactPage9(login.driver)
    add_new_contact.add_new_contact()
    add_new_contact.firstname(ConfigAddNewContact9.FIRSTNAME9)
    add_new_contact.lastname(ConfigAddNewContact9.LASTNAME9)
    add_new_contact.dob(ConfigAddNewContact9.DOB9)
    add_new_contact.email(ConfigAddNewContact9.EMAIL9)
    add_new_contact.number(ConfigAddNewContact9.NUMBER9)
    add_new_contact.street(ConfigAddNewContact9.STREET9)
    add_new_contact.city(ConfigAddNewContact9.CITY9)
    add_new_contact.state(ConfigAddNewContact9.STATE9)
    add_new_contact.postal(ConfigAddNewContact9.POSTAL9)
    add_new_contact.country(ConfigAddNewContact9.COUNTRY9)
    add_new_contact.submit()


def test_logout(login):
    logout_page = LogoutPage(login.driver)
    logout_page.logout()
