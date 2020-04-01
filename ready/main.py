


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

#My script imports
from login import Login
from delete import delete_all
from hot_uk_deals import scrape_hotukdeals
from hot_uk_restaurants import hotuk_res
from bella_italia import scrape_bella
from ask_italia import scrape_ask_italian
from deal_automation import Automation
from pyvirtualdisplay import Display
 
 
 
#Important
display = Display(visible=0, size=(800, 600))
display.start()


#Instantiate driver
driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')


def main():
    ####### BRAIN BOX #####################################


    login = Login(driver=driver)
    login.login(email="collinsanele@gmail.com", passwd="housewife")
    

    #Delete previous posts to prevent duplicates
    delete_all(driver=driver)



    try:
        bella = scrape_bella(driver=driver)
    except:
        bella = []
        pass

    try:
        uk_deals = scrape_hotukdeals(driver=driver)
    except:
        uk_deals = []
        pass

    try:
        ask_italia = scrape_ask_italian(driver=driver)
    except:
        ask_italia = []
        pass

    try:
        uk_deals_restaurants = hotuk_res(driver=driver)

    except Exception as e:
        print(e)
        uk_deals_restaurants  = []
        pass



    ########################################################################################
    automate = Automation(driver=driver)


    for item in bella:
        try:
            automate.deals(title_text=item["Title"], post_text=item["Body"], 
                       is_groceries=False, post_url=item["Urls"], google_map_url=item["Google_Link"])
        except Exception:
            pass


    for item in uk_deals:
        try:
            automate.deals(title_text=item["Title"], post_text=item["Body"], is_groceries=True, post_url=item["Urls"])
        except Exception:
            pass




    for item in ask_italia:
        try:
            automate.deals(title_text=item["Title"], post_text=item["Body"], 
                       is_groceries=False, post_url=item["Urls"], google_map_url=item["Google_Link"]) 
        except Exception:
            pass


    for item in uk_deals_restaurants:
        try:
            automate.deals(title_text=item["Titles"], post_text=item["Body"], 
                       is_groceries=False, post_url=item["Urls"], google_map_url=item["Google_Link"])

        except Exception as e:
            #print(e)
            pass  

        
        

if __name__ == "__main__":
    main()
