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






############# SCRAPE HOTUKDEAL #######################################################

def scrape_hotukdeals(driver):
    try:
        driver.get("https://www.hotukdeals.com/tag/groceries")
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "thread-title--list")))
        
        #Select London
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
        

        #Have to do again to prevent stale element error
        driver.get("https://www.hotukdeals.com/tag/groceries")
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "thread-title--list")))

        titles = [item.text for item in driver.find_elements_by_class_name("thread-title--list")]
        urls = [item.get_attribute("href") for item in driver.find_elements_by_class_name("thread-title--list")]
        results = [{"Title":titles[index], "Urls":urls[index], "Body":""} for index,item in enumerate(titles)]

        for index, item in enumerate(results[0:]):
            driver.get(item["Urls"])
            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "cept-description-container")))
            body = driver.find_element_by_class_name("cept-description-container").text
            results[index]["Body"] = body

        return results

    except Exception as e:
        print(e)
        pass
    