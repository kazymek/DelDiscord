# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: url.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def get_login_page(driver):
    try:
        driver.get("https://discord.com/login")

    except:
        print("Couldn't go to the discord login page: https://discord.login/ .")

def is_url_at_me(driver):
    try:
        WebDriverWait(driver=driver, timeout=10).until(expected_conditions.url_to_be("https://discord.com/channels/@me"))

    except:
        print("Isn't on the https://discord.com/channels/@me page.")