from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
website_link = 'https://www.daraz.com.bd/'
driver.get(website_link)
signup_button=driver.find_element(By.LINK_TEXT,"Sign Up")
signup_button.click()
signup_phone=driver.find_element("xpath","//input[contains(@placeholder,'Please enter')]")
signup_phone.send_keys("01728059676")
singup_password=driver.find_element("xpath","//input[contains(@placeholder,'Minimum 6 characters')]")
singup_password.send_keys("nipa123@")
singup_name=driver.find_element("xpath","//input[contains(@placeholder,'Enter your first and last name')]")
singup_name.send_keys("Nipa Dey")
send_verification_code=driver.find_element("xpath","//button[text()='Send']")
send_verification_code.click()
singup=driver.find_element("xpath","//button[text()='SIGN UP']")
singup.click()

