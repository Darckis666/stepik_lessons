import os
import time
from selenium import webdriver

link="http://suninjuly.github.io/file_input.html"
file="file.txt"

try:
     browser=webdriver.Chrome()
     browser.get(link)

     firstname=browser.find_element_by_name("firstname")
     firstname.send_keys("familiya")

     lastname=browser.find_element_by_name("lastname")
     lastname.send_keys("familiya")

     email=browser.find_element_by_name("email")
     email.send_keys("email@test.com")

     current_dir=os.path.abspath(os.path.dirname(__file__))
     file_path=os.path.join(current_dir, file)
     download_file=browser.find_element_by_id("file")
     download_file.send_keys(file_path)
     
     button=browser.find_element_by_css_selector("button.btn")
     button.click()
finally:
    time.sleep(15)
    browser.quit()
