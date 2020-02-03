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




##### DEAL AUTOMATION ###########################
    
       
def make_deal(driver):
    deals_chbox = driver.find_element_by_id("in-category-106")
    deals_chbox.click()
    
    
    
def tick_groceries(driver):
    driver.find_element_by_xpath("""//*[@id="in-popular-event-categories-144"]""").click()
    
    
    
def select_london(driver):
    filterBtn = driver.find_element_by_class_name("subNavMenu-btn")
    driver.execute_script("arguments[0].click();", filterBtn)
    submit_btn = driver.find_element_by_xpath("""//*[@id="feed-settings"]/div/div[2]/button""")
    innerLabel = driver.find_element_by_class_name("multiSelect-label")
    driver.execute_script("arguments[0].click();", innerLabel)

    chbox = driver.find_element_by_class_name("checkbox-text")
    driver.execute_script("arguments[0].click();", chbox)

    london_chbox = driver.find_element_by_xpath("""//*[@id="feed-settings"]/div/div[1]/div[2]/div/div[4]/label/span[1]/span""")
    driver.execute_script("arguments[0].click();", london_chbox)
    driver.execute_script("arguments[0].click();", submit_btn)
    driver.delete_all_cookies()

       
def handle_date(driver):
    try:

        date_start_input = driver.find_element_by_id("em-form-when").find_elements_by_tag_name("input")[0]
        date_end_input= driver.find_element_by_id("em-form-when").find_elements_by_tag_name("input")[2]

        day = datetime.datetime.now().date().day
        month = datetime.datetime.now().date().month
        year = datetime.datetime.now().date().year

        future_date = datetime.datetime.now() + timedelta(days=14)

        future_day = future_date.day
        future_month = future_date.month
        future_year = future_date.year

        date_start_input.clear()
        date_start_input.send_keys(f"{day}/{month}/{year}")
        date_end_input.clear()
        date_end_input.send_keys(f"{future_day}/{future_month}/{future_year}")



    except Exception as e:
        print(e)
        pass 
   



class Automation:
    def __init__(self, driver):
        self.driver = driver 
    
    
    
    def deals(self, title_text, post_text, is_groceries=False, post_url=None, google_map_url=None ):
        try:
            url = "https://www.citymealdeals.co.uk/wp-admin/post-new.php?post_type=event"
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "title")))
            title_input = self.driver.find_element_by_id("title")
            title_input.clear()
            show_body_textarea_btn = self.driver.find_element_by_id("content-html")
            self.driver.execute_script("arguments[0].click();", show_body_textarea_btn )
            body_textarea = self.driver.find_element_by_id("content")
            body_textarea.clear()
            title_input.send_keys(title_text.strip())
            body_textarea.send_keys(post_text.strip())
            most_used_tab = lambda:self.driver.find_element_by_xpath("""//*[@id="event-categories-tabs"]/li[2]/a""")
            self.driver.execute_script("arguments[0].click();", most_used_tab())
            
            

            if not is_groceries:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath("""//*[@id="in-popular-event-categories-678"]"""))
                target_url = self.driver.find_element_by_xpath("""//*[@id="em_attribute_1"]/td[2]/input""")
                food_url = self.driver.find_element_by_xpath("""//*[@id="em_attribute_2"]/td[2]/input""")
                target_url.clear()
                food_url.clear()
                target_url.send_keys(post_url)
                food_url.send_keys(google_map_url)
                
            
            else:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath("""//*[@id="in-popular-event-categories-144"]"""))
                
                try:
                    target_url = self.driver.find_element_by_xpath("""//*[@id="em_attribute_1"]/td[2]/input""")
                    target_url.send_keys(post_url)
                    
                except Exception as e:
                    print(e)
                    pass


            handle_date(driver=self.driver)


            
            self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_id("no-location"))
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "publish")))
            publish_btn = self.driver.find_element_by_id("publish")
            self.driver.execute_script("arguments[0].click();", publish_btn)
            print("Published")
                
        except Exception as e:
            print(e)
            pass





