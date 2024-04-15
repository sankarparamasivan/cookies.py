from requests import session
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class saucedemo:

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen. Then waits for 3 seconds
        :return:
        """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def login(self):
        self.boot()
        # This is to fill the username and the password
        self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
        sleep(3)
        self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
        sleep(3)
        # find the login button and click on it
        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(3)
        
    def cookie(self):
        cookies = self.driver.get_cookies()

        for cookie in cookies:
            file1 = open("MyFile.txt", "w")
            print(cookie)

        

obj = saucedemo()
obj.login()
obj.cookie()


