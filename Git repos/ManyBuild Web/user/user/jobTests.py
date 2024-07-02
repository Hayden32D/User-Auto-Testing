'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars

def job_tests_runner(driver):

    wait = WebDriverWait(driver, 10)

    def job1():
        try:
            tab_open = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__getavailabledetail")))
            tab_open.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__getavailabledetail"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.JOB_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = 




        except Exception as e:
            print(e)
            '''