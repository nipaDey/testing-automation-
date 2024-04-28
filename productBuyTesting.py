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


#loging testing
# login_button=driver.find_element(By.LINK_TEXT,"Login")
# login_button.click()
#
# login_phone_number=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your Phone Number or Email')]")
# login_phone_number.send_keys("01754606268")
#
# login_password=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your password')]")
# login_password.send_keys("Ashikdas68#")
#
# login=driver.find_element("xpath","//button[text()='LOGIN']")
# login.click()



# searching product , select product & add to cart product then loging for place to order
time.sleep(2)
search_product=driver.find_element("xpath","//input[@type='search']")
search_product.send_keys("head")

WebDriverWait(driver,2).until(EC.visibility_of_all_elements_located(("xpath",("//a[contains(@class,'suggest-common')]"))))
headphone_options=driver.find_elements("xpath","//a[contains(@class,'suggest-common')] ")
for index,option in enumerate(headphone_options):
    # print(f"link present in {index+1}  option:{option.get_attribute('href')}")
    # print(f"text present in {index+1} option: {option.text}")

    if "Headphone bluetooth" in option.text:
        option.click()
        driver.window_handles
        break
else:
    print("headphone options not found")



print(driver.window_handles)

driver.switch_to.window(driver.window_handles[0])


headphone_bluetooth=driver.find_element(By.XPATH,"(//div[@class='gridItem--Yd0sa'])[3]")
headphone_bluetooth.click()
time.sleep(2)

url=driver.current_url
print(f"URL for selected product = {url}")

#
# driver.switch_to.window(driver.window_handles[1])
#

add_to_cart=driver.find_element("xpath","//span[text()='Add to Cart']")
add_to_cart.click()

iframe_login=driver.find_element("xpath","//iframe[@class='login-iframe']")
driver.switch_to.frame(iframe_login)


WebDriverWait(driver,3).until(EC.visibility_of_all_elements_located(("xpath",("//input[contains(@placeholder,'Please enter your Phone Number or Email')]"))))

popup_login_phone_number=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your Phone Number or Email')]")
popup_login_phone_number.send_keys("01754606268")

popup_login_password=driver.find_element("xpath","//input[contains(@placeholder,'Please enter your password')]")
popup_login_password.send_keys("Ashikdas68#")

popup_login=driver.find_element("xpath","//button[text()='LOGIN']")
popup_login.click()

driver.switch_to.default_content()
time.sleep(2)
add_cart_last=driver.find_element("xpath","//button[text()='GO TO CART']")
add_cart_last.click()

time.sleep(2)
proceed_to_checkout=driver.find_element("xpath","//button[text()='PROCEED TO CHECKOUT (1)']")
proceed_to_checkout.click()























