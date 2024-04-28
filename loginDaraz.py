from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
website_link = 'https://www.daraz.com.bd/'
driver.get(website_link)

login_button=driver.find_element(By.LINK_TEXT,"Login")
login_button.click()

login_phone_number=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your Phone Number or Email')]")
login_phone_number.send_keys("01754606268")

login_password=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your password')]")
login_password.send_keys("Ashikdas68#")

login=driver.find_element("xpath","//button[text()='LOGIN']")
login.click()
