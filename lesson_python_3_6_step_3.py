import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainClass():
    @pytest.mark.parametrize('number_lessons', ["236895","236896","236897","236898","236899","236903","236904","236905"])
    def test_answer(self, browser,number_lessons):
        link=f"https://stepik.org/lesson/{number_lessons}/step/1"
        browser.get(link)
        
        answer=calc()
        input_answer=WebDriverWait(browser,7).until(EC.presence_of_element_located((By.TAG_NAME,"textarea")))
        input_answer.send_keys(answer)

	send_button=WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.again-btn"))
        send_button.click()
        
        e_message=WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.smart-hints__feedback")))
        e_message_text=broswer.find_element_by_css_selector("pre.smart-hints__hint")
        message=e_message_text.text
        assert message=="Correct!", "Проверка ответа прошла неучадно"
