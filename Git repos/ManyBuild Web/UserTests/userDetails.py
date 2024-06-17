from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import newFileOpen
import time

#user details

def userDetails():

    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', r'C:/webdrivers/chromedriver.exe')

    chrome_options = webdriver.ChromeOptions()

    # Create a new instance of Chrome WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Wait for the Swagger UI element to be present
    wait = WebDriverWait(driver, 1.5)  # Adjust timeout as needed

    open_tab_button = wait.until(EC.element_to_be_clickable(By.ID, "operations-User-get_api_User_details"))
    open_tab_button.click()
    time.sleep(2)

    