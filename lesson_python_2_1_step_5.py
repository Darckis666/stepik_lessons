from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/math.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)

    input_answer=browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    checkbox_robot=browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    radio_robots_rule=browser.find_element_by_id("robotsRule")
    radio_robots_rule.click()

    button_submit=browser.find_element_by_css_selector("button.btn")
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
