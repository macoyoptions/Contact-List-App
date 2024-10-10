from selenium.webdriver.common.by import By


class LoginLocator:
    ENTER_EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    CLICK_SUBMIT = (By.ID, "submit")

# FOR NEGATIVE TEST, FILL IN EMAIL THAT IS ALREADY IN USE
    ENTER_OLD_EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    ENTER_PASSWORDD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    CLICK_SUBMITT = (By.ID, "submit")




