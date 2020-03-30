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



############## SCRAPE HOTUKDEALS RESTAURANT #################
def hotuk_res(driver):
    result_container = []
    urls = []
    titles = []
    bodies = []
    names = []

    driver.get("https://www.hotukdeals.com/tag/restaurant")
    cards = driver.find_elements_by_class_name("threadGrid")
     

    for card in cards[0:11]:
        url = ""
        title = ""
        name = ""

        try:
            url = card.find_element_by_class_name("threadGrid-title").find_element_by_tag_name("a").get_attribute("href")

        except Exception as e:
            #print(e)
            pass

        try:
            title = card.find_element_by_class_name("threadGrid-title").find_element_by_tag_name("a").text.strip()
        except Exception as e:
            #print(e)
            pass
        
        
        try:
            name = card.find_element_by_class_name("threadGrid-title").find_element_by_class_name("text--color-brandPrimary").text.strip()
        except Exception as e:
            #print(e)
            pass


        urls.append(url)
        titles.append(title)
        names.append(name)


    #https://www.google.com/maps/search/bella+italia/
    urls = [url for url in urls if url != ""]
    titles = [title for title in titles if title != ""]
    names = [name for name in names if name != ""]
    #google_map_links = [f'https://www.google.com/maps/search/{name.replace(" ", "+")}' for name in names]
    google_map_links = ['https://www.google.com/maps/search/'+name.replace(" ", "+") for name in names]
    
    
    for url in urls[0:]:
       
        body = ""

        try:
            driver.get(url)

        except Exception as e:
            print(e)
            pass

        try:
            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "cept-description-container")))
            body = driver.find_element_by_class_name("cept-description-container").text.strip()

        except Exception as e:
            print(e)
            pass

        bodies.append(body)
        
       
    for index, item in enumerate(urls):
        try:
            result_container.append({"Urls":urls[index], "Titles":titles[index], 
                                 "Names":names[index], 
                                 "Google_Link": google_map_links[index], "Body": bodies[index]})
            
        except Exception as e:
            #print(e)
            pass
        
    
        
       
    return result_container
