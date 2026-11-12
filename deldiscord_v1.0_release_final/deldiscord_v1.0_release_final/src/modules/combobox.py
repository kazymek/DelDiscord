# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: combobox.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from time import sleep
from random import uniform

def get_combobox(driver) -> WebElement | None:
    try:
        combobox_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[role="combobox"]')))

        combobox_element.click()

        return combobox_element

    except:
        print("Error.")

def type_in_combobox(combobox, display_name) -> None:
    try:
        sleep(0.5)

        for character in display_name:
            combobox.send_keys(character)

            sleep(uniform(0.1, 0.3))
            
    except:
        print("Error.")