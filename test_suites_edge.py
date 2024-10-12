import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

from AddNewContactPage.AddNewContact_test import AddNewContactPage
from ConfigEdge.Config_Edge import ConfigEdge, Configaddnewcontactedge, Configaddnewcontactedge1, \
    Configaddnewcontactedge2, Configaddnewcontactedge3, Configaddnewcontactedge4, Configaddnewcontactedge5, \
    Configaddnewcontactedge6, Configaddnewcontactedge7, Configaddnewcontactedge8, ConfigLoginedge, \
    ConfigNegativeLoginedge, Configaddnewcontactedge9
from LoginPage.Login_test import LoginPage
from LogoutPage.Logout_test import LogoutPage
from SignupPage.Signup_test import SignupPage


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
    signup_page.signup_url(ConfigEdge.BASEURL)
    return signup_page


def test_signup_page_contact_list(signup):
    signup.signup()
    signup.firstname(ConfigEdge.FIRSTNAME)
    signup.lastname(ConfigEdge.LASTNAME)
    signup.email(ConfigEdge.EMAIL)
    signup.password(ConfigEdge.PASSWORD)
    signup.submit()


def test_addnewcontact_contact_list(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact()
    addnewcontact.firstname(Configaddnewcontactedge.FIRSTNAME)
    addnewcontact.lastname(Configaddnewcontactedge.LASTNAME)
    addnewcontact.dob(Configaddnewcontactedge.DOB)
    addnewcontact.email(Configaddnewcontactedge.EMAIL)
    addnewcontact.number(Configaddnewcontactedge.NUMBER)
    addnewcontact.street(Configaddnewcontactedge.STREET)
    addnewcontact.city(Configaddnewcontactedge.CITY)
    addnewcontact.state(Configaddnewcontactedge.STATE)
    addnewcontact.postal(Configaddnewcontactedge.POSTAL)
    addnewcontact.country(Configaddnewcontactedge.COUNTRY)
    addnewcontact.submit()


def test_addnewcontact_contact_list1(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact1()
    addnewcontact.firstname1(Configaddnewcontactedge1.FIRSTNAME1)
    addnewcontact.lastname1(Configaddnewcontactedge1.LASTNAME1)
    addnewcontact.dob1(Configaddnewcontactedge1.DOB1)
    addnewcontact.email1(Configaddnewcontactedge1.EMAIL1)
    addnewcontact.number1(Configaddnewcontactedge1.NUMBER1)
    addnewcontact.street1(Configaddnewcontactedge1.STREET1)
    addnewcontact.city1(Configaddnewcontactedge1.CITY1)
    addnewcontact.state1(Configaddnewcontactedge1.STATE1)
    addnewcontact.postal1(Configaddnewcontactedge1.POSTAL1)
    addnewcontact.country1(Configaddnewcontactedge1.COUNTRY1)
    addnewcontact.submit1()


def test_addnewcontact_contact_list2(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact2()
    addnewcontact.firstname2(Configaddnewcontactedge2.FIRSTNAME2)
    addnewcontact.lastname2(Configaddnewcontactedge2.LASTNAME2)
    addnewcontact.dob2(Configaddnewcontactedge2.DOB2)
    addnewcontact.email2(Configaddnewcontactedge2.EMAIL2)
    addnewcontact.number2(Configaddnewcontactedge2.NUMBER2)
    addnewcontact.street2(Configaddnewcontactedge2.STREET2)
    addnewcontact.city2(Configaddnewcontactedge2.CITY2)
    addnewcontact.state2(Configaddnewcontactedge2.STATE2)
    addnewcontact.postal2(Configaddnewcontactedge2.POSTAL2)
    addnewcontact.country2(Configaddnewcontactedge2.COUNTRY2)
    addnewcontact.submit2()


def test_addnewcontact_contact_list3(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact3()
    addnewcontact.firstname3(Configaddnewcontactedge3.FIRSTNAME3)
    addnewcontact.lastname3(Configaddnewcontactedge3.LASTNAME3)
    addnewcontact.dob3(Configaddnewcontactedge3.DOB3)
    addnewcontact.email3(Configaddnewcontactedge3.EMAIL3)
    addnewcontact.number3(Configaddnewcontactedge3.NUMBER3)
    addnewcontact.street3(Configaddnewcontactedge3.STREET3)
    addnewcontact.city3(Configaddnewcontactedge3.CITY3)
    addnewcontact.state3(Configaddnewcontactedge3.STATE3)
    addnewcontact.postal3(Configaddnewcontactedge3.POSTAL3)
    addnewcontact.country3(Configaddnewcontactedge3.COUNTRY3)
    addnewcontact.submit3()


def test_addnewcontact_contact_list4(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact4()
    addnewcontact.firstname4(Configaddnewcontactedge4.FIRSTNAME4)
    addnewcontact.lastname4(Configaddnewcontactedge4.LASTNAME4)
    addnewcontact.dob4(Configaddnewcontactedge4.DOB4)
    addnewcontact.email4(Configaddnewcontactedge4.EMAIL4)
    addnewcontact.number4(Configaddnewcontactedge4.NUMBER4)
    addnewcontact.street4(Configaddnewcontactedge4.STREET4)
    addnewcontact.city4(Configaddnewcontactedge4.CITY4)
    addnewcontact.state4(Configaddnewcontactedge4.STATE4)
    addnewcontact.postal4(Configaddnewcontactedge4.POSTAL4)
    addnewcontact.country4(Configaddnewcontactedge4.COUNTRY4)
    addnewcontact.submit4()


def test_addnewcontact_contact_list5(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact5()
    addnewcontact.firstname5(Configaddnewcontactedge5.FIRSTNAME5)
    addnewcontact.lastname5(Configaddnewcontactedge5.LASTNAME5)
    addnewcontact.dob5(Configaddnewcontactedge5.DOB5)
    addnewcontact.email5(Configaddnewcontactedge5.EMAIL5)
    addnewcontact.number5(Configaddnewcontactedge5.NUMBER5)
    addnewcontact.street5(Configaddnewcontactedge5.STREET5)
    addnewcontact.city5(Configaddnewcontactedge5.CITY5)
    addnewcontact.state5(Configaddnewcontactedge5.STATE5)
    addnewcontact.postal5(Configaddnewcontactedge5.POSTAL5)
    addnewcontact.country5(Configaddnewcontactedge5.COUNTRY5)
    addnewcontact.submit5()


def test_addnewcontact_contact_list6(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact6()
    addnewcontact.firstname6(Configaddnewcontactedge6.FIRSTNAME6)
    addnewcontact.lastname6(Configaddnewcontactedge6.LASTNAME6)
    addnewcontact.dob6(Configaddnewcontactedge6.DOB6)
    addnewcontact.email6(Configaddnewcontactedge6.EMAIL6)
    addnewcontact.number6(Configaddnewcontactedge6.NUMBER6)
    addnewcontact.street6(Configaddnewcontactedge6.STREET6)
    addnewcontact.city6(Configaddnewcontactedge6.CITY6)
    addnewcontact.state6(Configaddnewcontactedge6.STATE6)
    addnewcontact.postal6(Configaddnewcontactedge6.POSTAL6)
    addnewcontact.country6(Configaddnewcontactedge6.COUNTRY6)
    addnewcontact.submit6()


def test_addnewcontact_contact_list7(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact7()
    addnewcontact.firstname7(Configaddnewcontactedge7.FIRSTNAME7)
    addnewcontact.lastname7(Configaddnewcontactedge7.LASTNAME7)
    addnewcontact.dob7(Configaddnewcontactedge7.DOB7)
    addnewcontact.email7(Configaddnewcontactedge7.EMAIL7)
    addnewcontact.number7(Configaddnewcontactedge7.NUMBER7)
    addnewcontact.street7(Configaddnewcontactedge7.STREET7)
    addnewcontact.city7(Configaddnewcontactedge7.CITY7)
    addnewcontact.state7(Configaddnewcontactedge7.STATE7)
    addnewcontact.postal7(Configaddnewcontactedge7.POSTAL7)
    addnewcontact.country7(Configaddnewcontactedge7.COUNTRY7)
    addnewcontact.submit7()


def test_addnewcontact_contact_list8(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact8()
    addnewcontact.firstname8(Configaddnewcontactedge8.FIRSTNAME8)
    addnewcontact.lastname8(Configaddnewcontactedge8.LASTNAME8)
    addnewcontact.dob8(Configaddnewcontactedge8.DOB8)
    addnewcontact.email8(Configaddnewcontactedge8.EMAIL8)
    addnewcontact.number8(Configaddnewcontactedge8.NUMBER8)
    addnewcontact.street8(Configaddnewcontactedge8.STREET8)
    addnewcontact.city8(Configaddnewcontactedge8.CITY8)
    addnewcontact.state8(Configaddnewcontactedge8.STATE8)
    addnewcontact.postal8(Configaddnewcontactedge8.POSTAL8)
    addnewcontact.country8(Configaddnewcontactedge8.COUNTRY8)
    addnewcontact.submit8()


def test_addnewcontact_contact_list9(signup):
    addnewcontact = AddNewContactPage(signup.driver)
    addnewcontact.addnewcontact9()
    addnewcontact.firstname9(Configaddnewcontactedge9.FIRSTNAME9)
    addnewcontact.lastname9(Configaddnewcontactedge9.LASTNAME9)
    addnewcontact.dob9(Configaddnewcontactedge9.DOB9)
    addnewcontact.email9(Configaddnewcontactedge9.EMAIL9)
    addnewcontact.number9(Configaddnewcontactedge9.NUMBER9)
    addnewcontact.street9(Configaddnewcontactedge9.STREET9)
    addnewcontact.city9(Configaddnewcontactedge9.CITY9)
    addnewcontact.state9(Configaddnewcontactedge9.STATE9)
    addnewcontact.postal9(Configaddnewcontactedge9.POSTAL9)
    addnewcontact.country9(Configaddnewcontactedge9.COUNTRY9)
    addnewcontact.submit9()


def test_logout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigLoginedge.EMAIL)
    loginpage.password(ConfigLoginedge.PASSWORD)
    loginpage.submit()


def test_signout(signup):
    logoutpage = LogoutPage(signup.driver)
    logoutpage.logout()


def test_negative_login_page_contact_list(signup):
    loginpage = LoginPage(signup.driver)
    loginpage.email(ConfigNegativeLoginedge.EMAIL)
    loginpage.password(ConfigNegativeLoginedge.PASSWORD)
    loginpage.submit()

