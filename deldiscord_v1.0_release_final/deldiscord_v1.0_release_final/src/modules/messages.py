# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: messages.py
# =========================================================

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import modules.combobox as combobox
import modules.inputs as inputs

import time

def delete_messages(driver, actions) -> None:
    deleted_messages_count: int = 0

    while True:
        try:
            seach_results: list = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^="search-result-"]')))

        except: 
            driver.refresh()
            
            try:
                WebDriverWait(driver=driver, timeout=10).until(expected_conditions.url_to_be(f"https://discord.com/channels/{inputs.guild_ID}"))

                combobox_element = combobox.get_combobox(driver)

                filter.filter_username_listbox(driver)

                combobox.type_in_combobox(combobox_element, inputs.display_name)

                filter.filter_displayname_listbox(driver)


            except:
                print(f"Isn't on the https://discord.com/channels/{inputs.guild_ID} page.")

                button_next = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[rel="next"]')))
                print("Found button_next.")
                button_prev = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[rel="prev"]')))
                print("Found button_prev.")

                button_next.click()
                time.sleep(0.5)
                button_prev.click()

                continue

        count: int = 0
        seach_results_lenght = len(seach_results)

        try:
            for seach_result in seach_results:
                message_username_and_timestamp_element = WebDriverWait(driver=driver, timeout=2).until(lambda driver: seach_result.find_element(By.CSS_SELECTOR, '[aria-labelledby*="message-username-"][aria-labelledby*=message-timestamp-]'))

                message_username_and_timestamp_element.click()

                actions.context_click(message_username_and_timestamp_element)
                actions.perform()

                try:
                    message_content_ = WebDriverWait(driver=driver, timeout=0.5).until(lambda driver: seach_result.find_element(By.CSS_SELECTOR, '[id^="message-content-"]'))

                    span = WebDriverWait(driver=driver, timeout=0.5).until(lambda driver: message_content_.find_element(By.CSS_SELECTOR, 'span'))

                    span_str = span.text

                except:
                    span_str = "Unknown"

                message_delete_element = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[id="message-delete"]')))

                message_delete_element.click()

                actionBar_ = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[class^="actionBar_"]')))

                actionBar_.click()

                critical_primary_ = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[class*="critical-primary_"]')))

                critical_primary_.click()

                count += 1
                deleted_messages_count += 1

                print(f"Message is deleted. Content: {span_str} - Message Count: {deleted_messages_count}")

            if count >= seach_results_lenght:
                button_next = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[rel="next"]')))

                if button_next.get_attribute("disabled"):
                    print("All messages are deleted. -> thank you for using it!")
                    
                    return

                else:
                    button_next.click()

        except:
            pass

        try:
            button_next = WebDriverWait(driver=driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[rel="next"]')))

        except:
            print("All messages are deleted. But one more is recommended! -> thank you for using it!")

            return