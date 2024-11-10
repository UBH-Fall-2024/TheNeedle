from bs4 import BeautifulSoup
import string
import requests
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scraper(url):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        username = driver.find_element(By.NAME, "user")
        password = driver.find_element(By.NAME, "pass")

        # nu login bypass
        username.send_keys('s0964265')
        password.send_keys('eHsdfvknbiovq7')

        # Submit the login form
        driver.find_element(By.XPATH, "//input[@type='submit']").click()            
        all_text = driver.page_source
        soup = BeautifulSoup(all_text, 'html.parser')

        for script in soup(['script', 'style']):
            script.decompose()

        text = soup.get_text()
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk) 
        driver.quit()
        return text
            
    except requests.RequestException as e:
        print(f"An error occurred while fetching the article: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
