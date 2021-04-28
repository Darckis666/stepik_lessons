from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
    return str(int(x)+int(y))

link="http://suninjuly.github.io/selects1.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_id("num1")
    x=x_element.text

    y_element=browser.find_element_by_id("num2")
    y=y_element.text

    select=Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(calc(x,y))

    button_submit=browser.find_element_by_css_selector("button.btn")
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()

