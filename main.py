import csv
from typing import List

import config as c

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest


def read_file() -> List:
    """
    Read the csv file
    :return: user logins
    """
    with open('users_login.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        return [row[0] for row in csv_reader]


def invite_users(users_login: List) -> None:
    """
    Add users to the channel
    :param users_login: list of user logins
    """
    try:
        client = TelegramClient('user', api_id=c.API_ID, api_hash=c.API_HASH)
        with client:
            client.loop.run_until_complete(client(InviteToChannelRequest(
                channel=c.CHAT_ID,
                users=users_login
            )))
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")


invite_users(read_file())
