import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

from AddNewContactPage.AddNewContact_test import AddNewContactPage
from LoginPage.Login_test import LoginPage
from LogoutPage.Logout_test import LogoutPage
from SignupPage.Signup_test import SignupPage
from config.config import Configaddnewcontact, Config, Configaddnewcontact1, Configaddnewcontact2, Configaddnewcontact3, \
    Configaddnewcontact4, Configaddnewcontact5, Configaddnewcontact6, Configaddnewcontact7, Configaddnewcontact8, \
    Configaddnewcontact9, ConfigLogin, ConfigNegativeLogin


@pytest.fixture(scope="session")
def driver_setup():
    edge_options = Options()
    # Uncomment the line below to run in headless mode
    edge_options.add_argument("--headless")  # Run Chrome in headless mode
    edge_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=edge_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def signup(driver_setup):
    driver = driver_setup
    signup_page = SignupPage(driver)
    signup_page.signup_url(Config.BASEURL)
    return signup_page


def test_signup_page_contact_list(signup):
    signup.signup()
    signup.firstname(Config.FIRSTNAME)
    signup.lastname(Config.LASTNAME)
    signup.email(Config.EMAIL)
    signup.password(Config.PASSWORD)
    signup.submit()


def test_addnewcontact_contact_list(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact()
    addnewcontact.firstname(Configaddnewcontact.FIRSTNAME)
    addnewcontact.lastname(Configaddnewcontact.LASTNAME)
    addnewcontact.dob(Configaddnewcontact.DOB)
    addnewcontact.email(Configaddnewcontact.EMAIL)
    addnewcontact.number(Configaddnewcontact.NUMBER)
    addnewcontact.street(Configaddnewcontact.STREET)
    addnewcontact.city(Configaddnewcontact.CITY)
    addnewcontact.state(Configaddnewcontact.STATE)
    addnewcontact.postal(Configaddnewcontact.POSTAL)
    addnewcontact.country(Configaddnewcontact.COUNTRY)
    addnewcontact.submit()


def test_addnewcontact_contact_list1(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact1()
    addnewcontact.firstname1(Configaddnewcontact1.FIRSTNAME1)
    addnewcontact.lastname1(Configaddnewcontact1.LASTNAME1)
    addnewcontact.dob1(Configaddnewcontact1.DOB1)
    addnewcontact.email1(Configaddnewcontact1.EMAIL1)
    addnewcontact.number1(Configaddnewcontact1.NUMBER1)
    addnewcontact.street1(Configaddnewcontact1.STREET1)
    addnewcontact.city1(Configaddnewcontact1.CITY1)
    addnewcontact.state1(Configaddnewcontact1.STATE1)
    addnewcontact.postal1(Configaddnewcontact1.POSTAL1)
    addnewcontact.country1(Configaddnewcontact1.COUNTRY1)
    addnewcontact.submit1()


def test_addnewcontact_contact_list2(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact2()
    addnewcontact.firstname2(Configaddnewcontact2.FIRSTNAME2)
    addnewcontact.lastname2(Configaddnewcontact2.LASTNAME2)
    addnewcontact.dob2(Configaddnewcontact2.DOB2)
    addnewcontact.email2(Configaddnewcontact2.EMAIL2)
    addnewcontact.number2(Configaddnewcontact2.NUMBER2)
    addnewcontact.street2(Configaddnewcontact2.STREET2)
    addnewcontact.city2(Configaddnewcontact2.CITY2)
    addnewcontact.state2(Configaddnewcontact2.STATE2)
    addnewcontact.postal2(Configaddnewcontact2.POSTAL2)
    addnewcontact.country2(Configaddnewcontact2.COUNTRY2)
    addnewcontact.submit2()


def test_addnewcontact_contact_list3(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact3()
    addnewcontact.firstname3(Configaddnewcontact3.FIRSTNAME3)
    addnewcontact.lastname3(Configaddnewcontact3.LASTNAME3)
    addnewcontact.dob3(Configaddnewcontact3.DOB3)
    addnewcontact.email3(Configaddnewcontact3.EMAIL3)
    addnewcontact.number3(Configaddnewcontact3.NUMBER3)
    addnewcontact.street3(Configaddnewcontact3.STREET3)
    addnewcontact.city3(Configaddnewcontact3.CITY3)
    addnewcontact.state3(Configaddnewcontact3.STATE3)
    addnewcontact.postal3(Configaddnewcontact3.POSTAL3)
    addnewcontact.country3(Configaddnewcontact3.COUNTRY3)
    addnewcontact.submit3()


def test_addnewcontact_contact_list4(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact4()
    addnewcontact.firstname4(Configaddnewcontact4.FIRSTNAME4)
    addnewcontact.lastname4(Configaddnewcontact4.LASTNAME4)
    addnewcontact.dob4(Configaddnewcontact4.DOB4)
    addnewcontact.email4(Configaddnewcontact4.EMAIL4)
    addnewcontact.number4(Configaddnewcontact4.NUMBER4)
    addnewcontact.street4(Configaddnewcontact4.STREET4)
    addnewcontact.city4(Configaddnewcontact4.CITY4)
    addnewcontact.state4(Configaddnewcontact4.STATE4)
    addnewcontact.postal4(Configaddnewcontact4.POSTAL4)
    addnewcontact.country4(Configaddnewcontact4.COUNTRY4)
    addnewcontact.submit4()


def test_addnewcontact_contact_list5(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact5()
    addnewcontact.firstname5(Configaddnewcontact5.FIRSTNAME5)
    addnewcontact.lastname5(Configaddnewcontact5.LASTNAME5)
    addnewcontact.dob5(Configaddnewcontact5.DOB5)
    addnewcontact.email5(Configaddnewcontact5.EMAIL5)
    addnewcontact.number5(Configaddnewcontact5.NUMBER5)
    addnewcontact.street5(Configaddnewcontact5.STREET5)
    addnewcontact.city5(Configaddnewcontact5.CITY5)
    addnewcontact.state5(Configaddnewcontact5.STATE5)
    addnewcontact.postal5(Configaddnewcontact5.POSTAL5)
    addnewcontact.country5(Configaddnewcontact5.COUNTRY5)
    addnewcontact.submit5()


def test_addnewcontact_contact_list6(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact6()
    addnewcontact.firstname6(Configaddnewcontact6.FIRSTNAME6)
    addnewcontact.lastname6(Configaddnewcontact6.LASTNAME6)
    addnewcontact.dob6(Configaddnewcontact6.DOB6)
    addnewcontact.email6(Configaddnewcontact6.EMAIL6)
    addnewcontact.number6(Configaddnewcontact6.NUMBER6)
    addnewcontact.street6(Configaddnewcontact6.STREET6)
    addnewcontact.city6(Configaddnewcontact6.CITY6)
    addnewcontact.state6(Configaddnewcontact6.STATE6)
    addnewcontact.postal6(Configaddnewcontact6.POSTAL6)
    addnewcontact.country6(Configaddnewcontact6.COUNTRY6)
    addnewcontact.submit6()


def test_addnewcontact_contact_list7(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact7()
    addnewcontact.firstname7(Configaddnewcontact7.FIRSTNAME7)
    addnewcontact.lastname7(Configaddnewcontact7.LASTNAME7)
    addnewcontact.dob7(Configaddnewcontact7.DOB7)
    addnewcontact.email7(Configaddnewcontact7.EMAIL7)
    addnewcontact.number7(Configaddnewcontact7.NUMBER7)
    addnewcontact.street7(Configaddnewcontact7.STREET7)
    addnewcontact.city7(Configaddnewcontact7.CITY7)
    addnewcontact.state7(Configaddnewcontact7.STATE7)
    addnewcontact.postal7(Configaddnewcontact7.POSTAL7)
    addnewcontact.country7(Configaddnewcontact7.COUNTRY7)
    addnewcontact.submit7()


def test_addnewcontact_contact_list8(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact8()
    addnewcontact.firstname8(Configaddnewcontact8.FIRSTNAME8)
    addnewcontact.lastname8(Configaddnewcontact8.LASTNAME8)
    addnewcontact.dob8(Configaddnewcontact8.DOB8)
    addnewcontact.email8(Configaddnewcontact8.EMAIL8)
    addnewcontact.number8(Configaddnewcontact8.NUMBER8)
    addnewcontact.street8(Configaddnewcontact8.STREET8)
    addnewcontact.city8(Configaddnewcontact8.CITY8)
    addnewcontact.state8(Configaddnewcontact8.STATE8)
    addnewcontact.postal8(Configaddnewcontact8.POSTAL8)
    addnewcontact.country8(Configaddnewcontact8.COUNTRY8)
    addnewcontact.submit8()


def test_addnewcontact_contact_list9(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact9()
    addnewcontact.firstname9(Configaddnewcontact9.FIRSTNAME9)
    addnewcontact.lastname9(Configaddnewcontact9.LASTNAME9)
    addnewcontact.dob9(Configaddnewcontact9.DOB9)
    addnewcontact.email9(Configaddnewcontact9.EMAIL9)
    addnewcontact.number9(Configaddnewcontact9.NUMBER9)
    addnewcontact.street9(Configaddnewcontact9.STREET9)
    addnewcontact.city9(Configaddnewcontact9.CITY9)
    addnewcontact.state9(Configaddnewcontact9.STATE9)
    addnewcontact.postal9(Configaddnewcontact9.POSTAL9)
    addnewcontact.country9(Configaddnewcontact9.COUNTRY9)
    addnewcontact.submit9()


def test_logout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigLogin.EMAIL)
    loginpage.password(ConfigLogin.PASSWORD)
    loginpage.submit()


def test_signout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_negative_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigNegativeLogin.EMAIL)
    loginpage.password(ConfigNegativeLogin.PASSWORD)
    loginpage.submit()

