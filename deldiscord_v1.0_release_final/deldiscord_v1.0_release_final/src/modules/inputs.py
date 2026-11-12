# =========================================================
# Name: DelDiscord
# Developer: k@zym3k
# License: GNU Affero General Public License v3.0 (AGPLv3)
# =========================================================
# File: inputs.py
# =========================================================

guild_ID = None
display_name = None

def get_email() -> str:
    email = input("What is your email?: ")

    return email

def get_password() -> str:
    password = input("What is your password?: ")

    return password

def get_guild_ID() -> str:
    global guild_ID

    guild_ID = input("What is the guild (server) ID: ")

    return guild_ID

def get_display_name() -> str:
    global display_name

    display_name = input("What is your display name?: ")

    return display_name