from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import newFileOpen
import globalVars
import time


# Get the Chrome WebDriver path from an environment variable
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', r'C:/webdrivers/chromedriver.exe')

# Check if the path to ChromeDriver is valid
if not os.path.isfile(chrome_driver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")

# Set up Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  # Uncomment for headless mode
chrome_options.add_argument('--start-maximized')

# Create a new instance of Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


#user methods
#user details

def userDetails():
    open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_details")))
    open_tab_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
    
    status_text = status_element.get_attribute('textContent')
    #print(status_text)
    #print 200
    print("Status for user details: " + status_text[0:3])
    status_num = int(status_text[0:3])

    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_details']/div[1]/button[1]")))
    close_tab.click()
    #time.sleep(2)

    if status_num == 200:
        print("API call successful (Status 200) for /api/User/details\n")
        return 200
    elif status_num == 401:
        print("Unauthorized access (Status 401) for /api/User/details\n")
        return 401
    else:
        print("Error")

def userDocs():
    open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_documents")))
    open_tab_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
    
    status_text = status_element.get_attribute('textContent')
    #print(status_text)
    #print 200
    print("Status for user details: " + status_text[0:3])
    status_num = int(status_text[0:3])

    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_documents']/div[1]/button[1]")))
    close_tab.click()
    #time.sleep(2)

    if status_num == 200:
        print("API call successful (Status 200) for /api/User/documents\n")
        return 200
    elif status_num == 401:
        print("Unauthorized access (Status 401) for /api/User/documents\n")
        return 401
    else:
        print("Error")

def userProfile():
    open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_profile")))
    open_tab_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
    
    status_text = status_element.get_attribute('textContent')
    #print(status_text)
    #print 200
    print("Status for user details: " + status_text[0:3])
    status_num = int(status_text[0:3])

    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_profile']/div[1]/button[1]")))
    close_tab.click()
    #time.sleep(2)

    if status_num == 200:
        print("API call successful (Status 200) for /api/User/Profile\n")
        return 200
    elif status_num == 401:
        print("Unauthorized access (Status 401) for /api/User/Profile\n")
        return 401
    else:
        print("Error")

def userProjects():
    open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_projects")))
    open_tab_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
    
    status_text = status_element.get_attribute('textContent')
    #print(status_text)
    #print 200
    print("Status for user details: " + status_text[0:3])
    status_num = int(status_text[0:3])

    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_projects']/div[1]/button[1]")))
    close_tab.click()

    if status_num == 200:
        print("API call successful (Status 200) for /api/User/Projects\n")
        return 200
    elif status_num == 401:
        print("Unauthorized access (Status 401) for /api/User/Projects\n")
        return 401
    else:
        print("Error")

def userSummary():
    open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_summary")))
    open_tab_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
    
    status_text = status_element.get_attribute('textContent')
    #print(status_text)
    #print 200
    print("Status for user details: " + status_text[0:3])
    status_num = int(status_text[0:3])

    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_summary']/div/button[1]")))
    close_tab.click()

    if status_num == 200:
        print("API call successful (Status 200) for /api/User/summary\n")
        return 200
    elif status_num == 401:
        print("Unauthorized access (Status 401) for /api/User/summary\n")
        return 401
    else:
        print("Error")


try:
    # Navigate to the Swagger UI
    driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html")

    # Wait for the Swagger UI element to be present
    wait = WebDriverWait(driver, 1.5)  # Adjust timeout as needed

    # Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
    login_button.click()

    # Click the "Try it out" button
    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    # Enter login details
    text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))
    text_field.clear()
    text_to_write = '{"userName": "HDouglas+Creator1@method-automation.com", "password": "Poohbear@32D"}'
    text_field.send_keys(text_to_write)
    #print("Text written to the text field: ", text_to_write)

    # Execute login
    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    # Wait for the response
    download = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.download-contents")))
    download.click()

    # Open the new file to get the key
    key = newFileOpen.openNewFile()
    #print(key)

    # Authorize with the obtained key
    authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
    authorize_button.click()

    key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
    key_input_field.send_keys("Bearer " + key)

    final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
    final_press_button.click()

    # Check if authorization was successful
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))

        close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.btn.modal-btn.auth.btn-done.button")))
        close.click()

        close_open_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        close_open_tab.click()
        time.sleep(2)
    except Exception as e:
        print("Authorization was not granted")

    #prints the 200 or 401 status of each user field; 200 is good, 401 is bad
    userDetailsNum = userDetails()
    userDocsNum = userDocs()
    userProfileNum = userProfile()
    userProjectsNum = userProjects()
    userSummaryNum = userSummary()
    

finally:
    # Ensure the browser is closed, even if an error occurs
    driver.quit()
