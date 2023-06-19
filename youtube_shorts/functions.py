import random
import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from typing import List


def get_element(driver: WebElement | webdriver.Remote, mark: tuple, tm: int = 15) -> WebElement | None:
    wait = WebDriverWait(driver, tm)
    try:
        element: WebElement = wait.until(EC.presence_of_element_located(mark))
        return element
    except TimeoutException:
        return None


def get_element_clickable(driver: WebElement | webdriver.Remote, mark: tuple, tm: int = 15) -> WebElement | None:
    wait = WebDriverWait(driver, tm)
    try:
        element: WebElement = wait.until(EC.element_to_be_clickable(mark))
        return element
    except TimeoutException:
        return None


def get_elements(driver: WebElement | webdriver.Remote, mark: tuple, tm: int = 15) -> WebElement | list:
    wait = WebDriverWait(driver, tm)
    try:
        elements: List[WebElement] = wait.until(EC.presence_of_all_elements_located(mark))
        return elements
    except TimeoutException:
        return []


def select_option_by_value(element: WebElement, option_value: int | str) -> None:
    select = Select(element)

    select.select_by_value(option_value)


def send_keys(element: WebElement, text, min_t=5000, max_t=15000, delay=True) -> None:
    text = str(text)
    if not delay:
        element.send_keys(text)
        return
    for letter in text:
        element.send_keys(letter)
        rsleep(min_t, max_t)


def xpath_text_lower(text):
    return f"contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text}')"


def rsleep(min_t=5000, max_t=35000):
    time.sleep(random.randint(min_t, max_t) * 0.0001)
