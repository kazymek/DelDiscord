# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: driver.py
# =========================================================

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

saved_driver = None

def create_driver() -> WebDriver | None:
    global saved_driver

    try:
        options = Options()

        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

        actions = ActionChains(driver=driver)

        saved_driver = driver

        return driver, actions

    except:
        print("Couldn't create a driver. Maybe you don't have Chrome. Official Chrome download website: https://www.google.com/chrome/ .")

def get_driver() -> WebDriver | None:
    try:
        if not saved_driver:
            create_driver()

            return

        return saved_driver
    
    except:
        print("Couldn't get the driver.")

        return None

def quit_driver(driver=None) -> None:
    global saved_driver

    try:
        if driver:
            driver.quit()

        elif saved_driver:
            saved_driver.quit()

        else:
            print("Couldn't quit the driver. Maybe the driver never existed")

    except:
        print("Couldn't quit the driver. It is possible that the driver is still open and taking your RAM. Go on Taskmanager, and close it manually or restart your computer.")