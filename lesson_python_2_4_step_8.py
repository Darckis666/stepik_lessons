from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/explicit_wait2.html"
price_wait="100";

try:
    browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
    
    price_element=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),price_wait))
    button=browser.find_element_by_id("book")
    button.click()
    
    x_element=browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)

    input_answer=browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button=browser.find_element_by_id("solve")
    button.click();


finally:
    time.sleep(15)
    browser.quit()
