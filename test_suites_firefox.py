import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from AddNewContactPage.AddNewContact_test import AddNewContactPage
from ConfigFirefox.Config_Firefox import ConfigFirefox, ConfigaddnewcontactFirefox, ConfigaddnewcontactFirefox1, \
    ConfigaddnewcontactFirefox2, ConfigaddnewcontactFirefox3, ConfigaddnewcontactFirefox4, ConfigaddnewcontactFirefox5, \
    ConfigaddnewcontactFirefox6, ConfigaddnewcontactFirefox7, ConfigaddnewcontactFirefox8, ConfigaddnewcontactFirefox9, \
    ConfigLoginFirefox, ConfigNegativeLoginFirefox
from LoginPage.Login_test import LoginPage
from LogoutPage.Logout_test import LogoutPage
from SignupPage.Signup_test import SignupPage


@pytest.fixture(scope="session")
def driver_setup():
    firefox_options = Options()
    # Uncomment the line below to run in headless mode
    firefox_options.add_argument("--headless")  # Run Chrome in headless mode
    firefox_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=firefox_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def signup(driver_setup):
    driver = driver_setup
    signup_page = SignupPage(driver)
    signup_page.signup_url(ConfigFirefox.BASEURL)
    return signup_page


def test_signup_page_contact_list(signup):
    signup.signup()
    signup.firstname(ConfigFirefox.FIRSTNAME)
    signup.lastname(ConfigFirefox.LASTNAME)
    signup.email(ConfigFirefox.EMAIL)
    signup.password(ConfigFirefox.PASSWORD)
    signup.submit()


def test_addnewcontact_contact_list(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact()
    addnewcontact.firstname(ConfigaddnewcontactFirefox.FIRSTNAME)
    addnewcontact.lastname(ConfigaddnewcontactFirefox.LASTNAME)
    addnewcontact.dob(ConfigaddnewcontactFirefox.DOB)
    addnewcontact.email(ConfigaddnewcontactFirefox.EMAIL)
    addnewcontact.number(ConfigaddnewcontactFirefox.NUMBER)
    addnewcontact.street(ConfigaddnewcontactFirefox.STREET)
    addnewcontact.city(ConfigaddnewcontactFirefox.CITY)
    addnewcontact.state(ConfigaddnewcontactFirefox.STATE)
    addnewcontact.postal(ConfigaddnewcontactFirefox.POSTAL)
    addnewcontact.country(ConfigaddnewcontactFirefox.COUNTRY)
    addnewcontact.submit()


def test_addnewcontact_contact_list1(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact1()
    addnewcontact.firstname1(ConfigaddnewcontactFirefox1.FIRSTNAME1)
    addnewcontact.lastname1(ConfigaddnewcontactFirefox1.LASTNAME1)
    addnewcontact.dob1(ConfigaddnewcontactFirefox1.DOB1)
    addnewcontact.email1(ConfigaddnewcontactFirefox1.EMAIL1)
    addnewcontact.number1(ConfigaddnewcontactFirefox1.NUMBER1)
    addnewcontact.street1(ConfigaddnewcontactFirefox1.STREET1)
    addnewcontact.city1(ConfigaddnewcontactFirefox1.CITY1)
    addnewcontact.state1(ConfigaddnewcontactFirefox1.STATE1)
    addnewcontact.postal1(ConfigaddnewcontactFirefox1.POSTAL1)
    addnewcontact.country1(ConfigaddnewcontactFirefox1.COUNTRY1)
    addnewcontact.submit1()


def test_addnewcontact_contact_list2(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact2()
    addnewcontact.firstname2(ConfigaddnewcontactFirefox2.FIRSTNAME2)
    addnewcontact.lastname2(ConfigaddnewcontactFirefox2.LASTNAME2)
    addnewcontact.dob2(ConfigaddnewcontactFirefox2.DOB2)
    addnewcontact.email2(ConfigaddnewcontactFirefox2.EMAIL2)
    addnewcontact.number2(ConfigaddnewcontactFirefox2.NUMBER2)
    addnewcontact.street2(ConfigaddnewcontactFirefox2.STREET2)
    addnewcontact.city2(ConfigaddnewcontactFirefox2.CITY2)
    addnewcontact.state2(ConfigaddnewcontactFirefox2.STATE2)
    addnewcontact.postal2(ConfigaddnewcontactFirefox2.POSTAL2)
    addnewcontact.country2(ConfigaddnewcontactFirefox2.COUNTRY2)
    addnewcontact.submit2()


def test_addnewcontact_contact_list3(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact3()
    addnewcontact.firstname3(ConfigaddnewcontactFirefox3.FIRSTNAME3)
    addnewcontact.lastname3(ConfigaddnewcontactFirefox3.LASTNAME3)
    addnewcontact.dob3(ConfigaddnewcontactFirefox3.DOB3)
    addnewcontact.email3(ConfigaddnewcontactFirefox3.EMAIL3)
    addnewcontact.number3(ConfigaddnewcontactFirefox3.NUMBER3)
    addnewcontact.street3(ConfigaddnewcontactFirefox3.STREET3)
    addnewcontact.city3(ConfigaddnewcontactFirefox3.CITY3)
    addnewcontact.state3(ConfigaddnewcontactFirefox3.STATE3)
    addnewcontact.postal3(ConfigaddnewcontactFirefox3.POSTAL3)
    addnewcontact.country3(ConfigaddnewcontactFirefox3.COUNTRY3)
    addnewcontact.submit3()


def test_addnewcontact_contact_list4(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact4()
    addnewcontact.firstname4(ConfigaddnewcontactFirefox4.FIRSTNAME4)
    addnewcontact.lastname4(ConfigaddnewcontactFirefox4.LASTNAME4)
    addnewcontact.dob4(ConfigaddnewcontactFirefox4.DOB4)
    addnewcontact.email4(ConfigaddnewcontactFirefox4.EMAIL4)
    addnewcontact.number4(ConfigaddnewcontactFirefox4.NUMBER4)
    addnewcontact.street4(ConfigaddnewcontactFirefox4.STREET4)
    addnewcontact.city4(ConfigaddnewcontactFirefox4.CITY4)
    addnewcontact.state4(ConfigaddnewcontactFirefox4.STATE4)
    addnewcontact.postal4(ConfigaddnewcontactFirefox4.POSTAL4)
    addnewcontact.country4(ConfigaddnewcontactFirefox4.COUNTRY4)
    addnewcontact.submit4()


def test_addnewcontact_contact_list5(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact5()
    addnewcontact.firstname5(ConfigaddnewcontactFirefox5.FIRSTNAME5)
    addnewcontact.lastname5(ConfigaddnewcontactFirefox5.LASTNAME5)
    addnewcontact.dob5(ConfigaddnewcontactFirefox5.DOB5)
    addnewcontact.email5(ConfigaddnewcontactFirefox5.EMAIL5)
    addnewcontact.number5(ConfigaddnewcontactFirefox5.NUMBER5)
    addnewcontact.street5(ConfigaddnewcontactFirefox5.STREET5)
    addnewcontact.city5(ConfigaddnewcontactFirefox5.CITY5)
    addnewcontact.state5(ConfigaddnewcontactFirefox5.STATE5)
    addnewcontact.postal5(ConfigaddnewcontactFirefox5.POSTAL5)
    addnewcontact.country5(ConfigaddnewcontactFirefox5.COUNTRY5)
    addnewcontact.submit5()


def test_addnewcontact_contact_list6(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact6()
    addnewcontact.firstname6(ConfigaddnewcontactFirefox6.FIRSTNAME6)
    addnewcontact.lastname6(ConfigaddnewcontactFirefox6.LASTNAME6)
    addnewcontact.dob6(ConfigaddnewcontactFirefox6.DOB6)
    addnewcontact.email6(ConfigaddnewcontactFirefox6.EMAIL6)
    addnewcontact.number6(ConfigaddnewcontactFirefox6.NUMBER6)
    addnewcontact.street6(ConfigaddnewcontactFirefox6.STREET6)
    addnewcontact.city6(ConfigaddnewcontactFirefox6.CITY6)
    addnewcontact.state6(ConfigaddnewcontactFirefox6.STATE6)
    addnewcontact.postal6(ConfigaddnewcontactFirefox6.POSTAL6)
    addnewcontact.country6(ConfigaddnewcontactFirefox6.COUNTRY6)
    addnewcontact.submit6()


def test_addnewcontact_contact_list7(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact7()
    addnewcontact.firstname7(ConfigaddnewcontactFirefox7.FIRSTNAME7)
    addnewcontact.lastname7(ConfigaddnewcontactFirefox7.LASTNAME7)
    addnewcontact.dob7(ConfigaddnewcontactFirefox7.DOB7)
    addnewcontact.email7(ConfigaddnewcontactFirefox7.EMAIL7)
    addnewcontact.number7(ConfigaddnewcontactFirefox7.NUMBER7)
    addnewcontact.street7(ConfigaddnewcontactFirefox7.STREET7)
    addnewcontact.city7(ConfigaddnewcontactFirefox7.CITY7)
    addnewcontact.state7(ConfigaddnewcontactFirefox7.STATE7)
    addnewcontact.postal7(ConfigaddnewcontactFirefox7.POSTAL7)
    addnewcontact.country7(ConfigaddnewcontactFirefox7.COUNTRY7)
    addnewcontact.submit7()


def test_addnewcontact_contact_list8(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact8()
    addnewcontact.firstname8(ConfigaddnewcontactFirefox8.FIRSTNAME8)
    addnewcontact.lastname8(ConfigaddnewcontactFirefox8.LASTNAME8)
    addnewcontact.dob8(ConfigaddnewcontactFirefox8.DOB8)
    addnewcontact.email8(ConfigaddnewcontactFirefox8.EMAIL8)
    addnewcontact.number8(ConfigaddnewcontactFirefox8.NUMBER8)
    addnewcontact.street8(ConfigaddnewcontactFirefox8.STREET8)
    addnewcontact.city8(ConfigaddnewcontactFirefox8.CITY8)
    addnewcontact.state8(ConfigaddnewcontactFirefox8.STATE8)
    addnewcontact.postal8(ConfigaddnewcontactFirefox8.POSTAL8)
    addnewcontact.country8(ConfigaddnewcontactFirefox8.COUNTRY8)
    addnewcontact.submit8()


def test_addnewcontact_contact_list9(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact9()
    addnewcontact.firstname9(ConfigaddnewcontactFirefox9.FIRSTNAME9)
    addnewcontact.lastname9(ConfigaddnewcontactFirefox9.LASTNAME9)
    addnewcontact.dob9(ConfigaddnewcontactFirefox9.DOB9)
    addnewcontact.email9(ConfigaddnewcontactFirefox9.EMAIL9)
    addnewcontact.number9(ConfigaddnewcontactFirefox9.NUMBER9)
    addnewcontact.street9(ConfigaddnewcontactFirefox9.STREET9)
    addnewcontact.city9(ConfigaddnewcontactFirefox9.CITY9)
    addnewcontact.state9(ConfigaddnewcontactFirefox9.STATE9)
    addnewcontact.postal9(ConfigaddnewcontactFirefox9.POSTAL9)
    addnewcontact.country9(ConfigaddnewcontactFirefox9.COUNTRY9)
    addnewcontact.submit9()


def test_logout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigLoginFirefox.EMAIL)
    loginpage.password(ConfigLoginFirefox.PASSWORD)
    loginpage.submit()


def test_signout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_negative_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigNegativeLoginFirefox.EMAIL)
    loginpage.password(ConfigNegativeLoginFirefox.PASSWORD)
    loginpage.submit()

