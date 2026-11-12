# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: login.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from time import sleep
from random import uniform

def send_email(driver, email) -> None:
    try:
        email_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.NAME, "email")))

        email_element.click()

        sleep(0.5)

        for character in email:
            email_element.send_keys(character)

            sleep(uniform(0.1, 0.3))

    except:
        print("Error.")

def send_password(driver, password) -> None:
    try:
        password_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.NAME, "password")))

        password_element.click()

        sleep(0.5)

        for character in password:
            password_element.send_keys(character)

            sleep(uniform(0.1, 0.3))

    except:
        print("Error.")

def get_login(driver) -> None:
    try:
        login_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))

        login_element.click()

    except Exception as e:
        print("Couldn't login. Maybe your email or password is wrong.")