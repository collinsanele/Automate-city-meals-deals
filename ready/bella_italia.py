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






########### SCRAPE BELLA ITALIA ########################
def scrape_bella(driver):
    results = []
    driver.get("https://www.bellaitalia.co.uk/italian-restaurant/uxbridge/intu-uxbridge")
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "navbar-offers")))
    offerBtn = driver.find_element_by_id("navbar-offers")
    driver.execute_script("arguments[0].click();", offerBtn)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "border")))
    offer_links = [item.find_element_by_tag_name("a").get_attribute("href") for item in driver.find_elements_by_class_name("border")]
    titles = [item.find_element_by_tag_name("h4").text for item in driver.find_elements_by_class_name("border")]

    for index, link in enumerate(offer_links[0:]):
        try:
            obj = {}
            driver.get(link)
            WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.CLASS_NAME, "offer-terms_conditions")))
            body = driver.find_element_by_class_name("offer-terms_conditions").find_element_by_tag_name("div").text.strip()
            obj["Title"] = titles[index].strip() + " at Bella Italia"
            obj["Body"] = body
            obj["Urls"] = offer_links[index].strip()
            obj["Google_Link"] = "https://www.google.co.uk/maps/search/bella+italia/"
            results.append(obj)

        except Exception as e:
            print(str(e)+" for bella")
            pass

    return results