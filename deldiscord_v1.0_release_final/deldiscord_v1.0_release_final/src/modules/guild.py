# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: guild.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def get_guild(driver, guild_ID) -> None:
    try:
        guild_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, f'[data-list-item-id="guildsnav___{guild_ID}"]')))

        guild_element.click()

    except:
        print("Couldn't go to the guild (server). Maybe your guild (server) ID is wrong.")