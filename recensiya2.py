from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_css_selector ("div.first_block:nth-child(1) input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector ("div.first_block:nth-child(2) input")
    input2.send_keys("Petrov")
    input2 = browser.find_element_by_css_selector ("div.first_block:nth-child(3) input")
    input2.send_keys("Petrov")

    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

  
    time.sleep(1)

    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
   
    welcome_text = welcome_text_elt.text

  
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
   
    time.sleep(10)
   
    browser.quit()
