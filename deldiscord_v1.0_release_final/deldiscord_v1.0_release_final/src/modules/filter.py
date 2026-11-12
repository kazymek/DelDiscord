# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: filter.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def filter_username_listbox(driver: WebDriver) -> None:
    try:
        try:
            layerContainers_: list = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '[class^="layerContainer_"]')))

        except:
            return

        for layerContainer_ in layerContainers_:
            try:
                clickTrapContainer_ = WebDriverWait(driver=driver, timeout=0.5).until(lambda driver: layerContainer_.find_element(By.CSS_SELECTOR, '[class^="clickTrapContainer_"]'))

            except:
                continue

            try:
                popout_ = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: clickTrapContainer_.find_element(By.CSS_SELECTOR, '[id^="popout_"]'))

            except:
                continue

            try:
                listbox_element = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: popout_.find_element(By.CSS_SELECTOR, '[role="listbox"]'))

            except:
                continue

            try:
                group_element = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: listbox_element.find_element(By.CSS_SELECTOR, '[role="group"]'))

            except:
                continue

            try:
                uid_: list = WebDriverWait(driver=driver, timeout=1).until(lambda driver: group_element.find_elements(By.CSS_SELECTOR, '[id^="uid_"]'))

                uid_[0].click()

            except:
                continue

        return
            
    except:
        print("Error.")

def filter_displayname_listbox(driver: WebDriverWait) -> None:
    try:
        try:
            layerContainers_: list = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '[class^="layerContainer_"]')))

        except:
            pass

        for layerContainer_ in layerContainers_:
            try:
                clickTrapContainer_ = WebDriverWait(driver=driver, timeout=0.5).until(lambda driver: layerContainer_.find_element(By.CSS_SELECTOR, '[class^="clickTrapContainer_"]'))

            except:
                continue

            try:
                popout_ = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: clickTrapContainer_.find_element(By.CSS_SELECTOR, '[id^="popout_"]'))

            except:
                continue

            try:
                listbox_element = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: popout_.find_element(By.CSS_SELECTOR, '[role="listbox"]'))

            except:
                continue

            try:
                group_element = WebDriverWait(driver=driver, timeout=0.2).until(lambda driver: listbox_element.find_element(By.CSS_SELECTOR, '[role="group"]'))

            except:
                continue

            try:
                uid_: list = WebDriverWait(driver=driver, timeout=1).until(lambda driver: group_element.find_elements(By.CSS_SELECTOR, '[id^="uid_"]'))

                uid_[0].click()

            except:
                continue

    except:
        print("Error.")