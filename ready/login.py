



#Main python imports

from selenium import webdriver
import time
from datetime import timedelta
import random
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import datetime







##### LOGIN ##########################################
class Login:
    def __init__(self, driver):
        self.driver = driver
        
        
    def login(self, email, passwd):
        try:
            self.driver.get("http://citymealdeals.co.uk/")
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            
        except Exception as e:
            print(e)
            pass
        
        try:
            loginBtn = self.driver.find_element_by_link_text("Log in")
            loginBtn.click()
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "user_login")))
            usernameInput = self.driver.find_element_by_id("user_login")
            passInput = self.driver.find_element_by_id("user_pass")
            submitLoginBtn = self.driver.find_element_by_id("wp-submit")
            usernameInput.send_keys(email)
            passInput.send_keys(passwd)
            submitLoginBtn.click()
        
        except Exception as e:
            #print(e)
            pass