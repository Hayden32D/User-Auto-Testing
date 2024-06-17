from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import newFileOpen
from globalVars import userID
from globalVars import id

# Get the Chrome WebDriver path from an environment variable
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', r'C:/webdrivers/chromedriver.exe')

# Check if the path to ChromeDriver is valid
if not os.path.isfile(chrome_driver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")

# Set up Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  # Uncomment for headless mode

# Create a new instance of Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

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
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.download-contents")))

    # Open the new file to get the key
    key = newFileOpen.openNewFile()
    #print(key)

    # Authorize with the obtained key
    authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
    authorize_button.click()

    key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
    key_input_field.send_keys(key)

    final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
    final_press_button.click()

    # Check if authorization was successful
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))
        print("\nTest was a Success! Access Granted")
    except Exception as e:
        print("Authorization was not granted")

finally:
    # Ensure the browser is closed, even if an error occurs
    driver.quit()
