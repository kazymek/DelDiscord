# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: main.py
# =========================================================

import modules.driver as d
import modules.url as url
import modules.inputs as inputs
import modules.login as login
import modules.guild as guild
import modules.combobox as combobox
import modules.filter as filter
import modules.messages as messages

from modules.stop import stop

from time import sleep

def main() -> None:
    try:
        driver, actions = d.create_driver()

        if not driver:
            print("Driver couldn't be created!")

            stop()

            return

        email = inputs.get_email()
        password = inputs.get_password()
        guild_ID = inputs.get_guild_ID()
        display_name = inputs.get_display_name()
        
        url.get_login_page(driver)

        login.send_email(driver, email)

        login.send_password(driver, password)

        login.get_login(driver)

        url.is_url_at_me(driver)

        guild.get_guild(driver, guild_ID)

        combobox_element = combobox.get_combobox(driver)

        filter.filter_username_listbox(driver)

        combobox.type_in_combobox(combobox_element, display_name)

        filter.filter_displayname_listbox(driver)

        messages.delete_messages(driver, actions)

        sleep(60)

        d.quit_driver(driver)

    except Exception as e:
        print("CRITICAL ERROR: SOMETHING WENT WRONG!")

        # print(e)

        d.quit_driver()

if __name__ == "__main__":
    print("Don't start this pogram with this file. Search for the run file to start this program.")