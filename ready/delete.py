
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






######### DELETE FUNCTION TO CLEAR ALL DEALS ######################
def delete_all(driver):
    try:
        driver.get("https://www.citymealdeals.co.uk/wp-admin/edit.php?post_type=event")
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.ID, "search-submit")))

    except Exception as e:
        print(e)
        pass

    try:
        total_page_no = int(driver.find_element_by_class_name("total-pages").text.strip())

    except Exception as e:
        #print(e)
        total_page_no = 0
        pass

    #for loop to ensure all items are trashed
    #Double for loop because due to some weird reasons
    #all the items are not deleted in the first run
    for _ in range(3):
        for num in range(1, 3):
            try:
                #url = f"https://www.citymealdeals.co.uk/wp-admin/edit.php?post_type=event&paged={num}"
                url = "https://www.citymealdeals.co.uk/wp-admin/edit.php?post_type=event&paged="+str(num)
                driver.get(url)
                WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "cb-select-all-1")))
                all_offers_check_box = driver.find_element_by_id("cb-select-all-1")
                all_offers_check_box.click()
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                bulk_action_dropdowns = driver.find_element_by_xpath("""//*[@id="posts-filter"]/div[2]/div[1]/select""").find_elements_by_tag_name("option")


                for item in bulk_action_dropdowns:
                    if item.text.strip() == "Move to Trash":
                        item.click()

                apply_btn = driver.find_element_by_id("doaction2")
                driver.execute_script("arguments[0].click()", apply_btn)
                time.sleep(2)

            except Exception as e:
                print(e)
                pass

        
        
        
        
        


