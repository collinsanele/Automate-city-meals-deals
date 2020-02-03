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



######### SCRAPE ASKITALIA ###########################################
def scrape_ask_italian(driver):
    results = []
    driver.get("http://offers.askitalian.co.uk/")
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, """//*[@id="home"]/div[3]/div/header/div/nav/div/div/div[2]/a[2]""")))
    offersBtn = driver.find_element_by_xpath("""//*[@id="home"]/div[3]/div/header/div/nav/div/div/div[2]/a[2]""")
    driver.execute_script("arguments[0].click();", offersBtn)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,"""//*[@id="home"]/div[3]/div/main/section[2]/div[1]/div/div/div/div[5]/div/button/span""")))
    search_input = driver.find_element_by_class_name("js-search-term")
    search_input.clear()
    search_input.send_keys("LONDON")
    search_input.send_keys(u'\ue007')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME,("js-location-filter"))))
    londons = driver.find_element_by_xpath("""//*[@id="home"]/div[3]/div/main/section[2]/div[1]/div/div/div/div""").find_elements_by_tag_name("a")
    londons[0].click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME,("js-view-restaurant-offers"))))
    viewBtns= driver.find_elements_by_class_name("js-view-restaurant-offers")

    for viewBtn in viewBtns[0:1]:
        driver.execute_script("arguments[0].click();", viewBtn)

    WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.CLASS_NAME,("js-offers-heading"))))
    titles = [item.text.strip() for item in driver.find_elements_by_class_name("js-offers-heading")]
    titles = [item + " @ Azzuri Restaurants Limited" for item in titles]
    body = [item.text.strip() for item in driver.find_elements_by_class_name("js-offers-description")]
    urls = [item.get_attribute("href") for item in driver.find_elements_by_class_name("highlight")]
    

    for index, title in enumerate(titles):
        obj = {}
        obj["Title"] = title
        obj["Body"] = body[index]
        obj["Urls"] = urls[index]
        obj["Google_Link"] = "https://www.google.co.uk/maps/search/ask+italia"
        results.append(obj)

    return results